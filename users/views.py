from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
# 需要添加以下导入
import re
import random
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import CustomUser
import threading

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 注册后自动登录（可选）
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

# 使用Django内置视图处理登录/登出  自定义
class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    def get_success_url(self):
        # 动态跳转示例：根据用户角色跳转不同页面
        if self.request.user.is_superuser:
            return reverse('admin:index')
        return reverse('fate_index')  # 使用路由名称更安全

class CustomLogoutView(LogoutView):
    next_page = 'login'  # 登出后跳转至登录页


# views.py（新增部分）
from django.views.decorators.http import require_POST
from django.core.cache import cache

# 异步发送邮件函数
def send_mail_async(subject, message, from_email, recipient_list, fail_silently=False):
    def _send_mail():
        try:
            send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                fail_silently=fail_silently
            )
            print(f"邮件发送成功: {recipient_list}")
        except Exception as e:
            print(f"邮件发送失败: {str(e)}")
    
    # 创建并启动线程
    thread = threading.Thread(target=_send_mail)
    thread.start()
    return thread

@require_POST
def send_email_code(request):
    """发送邮箱验证码"""
    email = request.POST.get('email')
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        return JsonResponse({'code': 400, 'msg': '邮箱格式错误'})

    # 频率控制（60秒内不能重复发送）
    if cache.get(f'email_cooldown_{email}'):
        return JsonResponse({'code': 400, 'msg': '发送过于频繁'})

    # 生成6位随机验证码
    code = ''.join(random.choices('0123456789', k=6))
    
    # 存储验证码（5分钟有效）
    cache.set(f'login_code_{email}', code, 300)
    
    # 设置发送冷却（60秒）
    cache.set(f'email_cooldown_{email}', '1', 60)

    # 打印验证码到控制台（调试用）
    print(f"发送验证码到 {email}: {code}")

    # 异步发送邮件
    send_mail_async(
        '您的登录验证码',
        f'验证码：{code}（5分钟内有效）',
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False
    )
    
    # 立即返回响应，不等待邮件发送完成
    if settings.DEBUG:
        return JsonResponse({'code': 200, 'msg': f'验证码已发送（测试环境）: {code}'})
    return JsonResponse({'code': 200, 'msg': '验证码已发送，请注意查收'})

@require_POST
def email_code_login(request):
    """验证码登录"""
    email = request.POST.get('email')
    code = request.POST.get('code')

    # 验证码校验
    cached_code = cache.get(f'login_code_{email}')
    if not cached_code or cached_code != code:
        return JsonResponse({'code': 400, 'msg': '验证码错误'})

    # 自动创建用户（适配你的CustomUser模型）
    try:
        user = CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        user = CustomUser.objects.create_user(
            email=email,
            username='',  # 设置空字符串作为默认值
            phone=''  
        )
        user.set_unusable_password()
        user.save()

    # 执行登录
    login(request, user)
    return JsonResponse({'code': 200, 'msg': '登录成功'})