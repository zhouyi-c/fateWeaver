from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


class IndexView(TemplateView):
    template_name = "fate/index.html"  # 指定模板路径
    login_url = '/users/login/'  # 指定登录页路径
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tech_stack'] = [
            {'name': 'Django', 'icon': 'https://img.icons8.com/color/48/000000/django.png', 'description': '后端开发框架'},
            {'name': 'Vue.js', 'icon': 'https://img.icons8.com/color/48/000000/vuejs.png', 'description': '前端框架'},
            {'name': 'MySQL', 'icon': 'https://img.icons8.com/color/48/000000/mysql.png', 'description': '数据库系统'}
        ]
        return context

    
