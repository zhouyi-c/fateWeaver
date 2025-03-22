"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.20.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

from django.conf.global_settings import AUTH_USER_MODEL, LANGUAGES
from numpy.f2py.symbolic import Language

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-7xj!%7l$prve)u9rk&8u#pa_s&tpm#a0%=_)ub)##2(5trgld-"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "fate",
    "users"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates'),
        os.path.join(BASE_DIR, 'users/templates')
        
        
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "fateweaver",
        "USER": "root",
        "PASSWORD": "qazwsx",
        "HOST": "localhost",
        "PORT": 3306,
    }

}

AUTH_USER_MODEL = "users.CustomUser"
LOGIN_URL = '/users/login/'
# config/base.py
LOGIN_REDIRECT_URL = '/fate/'  # 指向Fate应用的根路径
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [

]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en"

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True


LANGUAGES = [
    ('en', 'English'),
    ('zh-hans', '简体中文'),
]

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "fate" / "static",
]  # 静态文件目录

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# settings.py
# 开发环境下使用控制台邮件后端
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.qq.com'  # 替换为你的邮箱服务商 SMTP 地址
    EMAIL_PORT = 465
    EMAIL_USE_SSL = True  # 使用SSL而不是TLS
    EMAIL_USE_TLS = False
    EMAIL_HOST_USER = 'zhou_chi@foxmail.com'  # 发件邮箱
    EMAIL_HOST_PASSWORD = 'ikanpaiteowkjdhh'  # 邮箱密码或应用专用密码
    DEFAULT_FROM_EMAIL = 'zhou_chi@foxmail.com'  # 必须与 EMAIL_HOST_USER 一致