from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='邮箱', unique=True)
    
    username = models.CharField(
        verbose_name='用户名',
        max_length=150,
        unique=False,  # 明确取消唯一性
        blank=True,
        null=False,    # 禁止数据库存储NULL
        default='',     # 默认值为空字符串
        help_text="可选，可随时修改"
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # 确保Django版本支持空列表

    phone = models.CharField(max_length=15, blank=True, verbose_name='手机号')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户管理'