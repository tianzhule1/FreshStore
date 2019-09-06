"""
Django settings for DjangoFresh project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#_*g#)k=c6jjy$cb)2tc&7sz^w)=vj92_-=1j80%=69ezgkrlu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ["*"]#让所有ip访问
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Store',
    'Buyer',
    'ckeditor',#富文本配置，django自带
    'ckeditor_uploader',
    'rest_framework',
    'djcelery',#django-celery;celery定时任务
]

MIDDLEWARE = [
    #'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'DjangoFresh.middleware.MiddlewareTest',#middleware中间件
]
ROOT_URLCONF = 'DjangoFresh.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DjangoFresh.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {#数据库配置
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'#简体字

TIME_ZONE = 'Asia/Shanghai'#指定时区

USE_I18N = True

USE_L10N = True

USE_TZ = False#为True默认使用utc 0时区
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS=(
    os.path.join(BASE_DIR,"static"),
)
MEDIA_URL="/media/"#长传文件
MEDIA_ROOT=os.path.join(BASE_DIR,"static")
# STATIC_ROOT=os.path.join(BASE_DIR,"static")#收集静态文件
CKEDITOR_UPLOAD_PATH='static/upload'
CKEDITOR_IMAGE_BACKEND="pillow"#富文本配置
#配置完富文本后要收集静态文件，然后在前端引用，然后运行
REST_FRAMEWORK={
    "DEFAULT_PERMISSION_CLASSES":[
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE':10,#分页需要,用于后端分页
    "DEFAULT_RENDERER_CLASSES":(
        'utils.rendererresponse.customrenderer',
    ),
    'DEFAULT_FILTER_BACKENDS':(
        'django_filters.rest_framework.DjangoFilterBackend',#django-filter自带查询过滤器

    )
}
#配置邮件服务器
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'#发送邮件采用smtp服务
EMAIL_USE_TLS=False#使用tls方式
EMAIL_HOST="smtp.163.com"
EMAIL_POST=465
EMAIL_HOST_USER="18232951692@qq.com"
EMAIL_HOST_PASSWORD="123aoe"
DEFAUIL_FROM_EMAIL="3303236612@qq.com"
#配置邮件服务器
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'#发送邮件采用smpt服务
#backend后端，后端设计backend,backend;core核心要点core,core,core核心core;mail邮件mail,mail;email电子邮件email;
#smpt简单邮件传输协议smpt,smpt,smpt;emailbackend
EMAIL_USE_TLS=False#TLS传输层安全协议TLS传输层安全协议
EMAIL_HOST="smpt.163.com"#HOST主机，主机163邮箱
EMAIL_POST=465#163邮箱加密传输用465端口
EMAIL_HOST_USER="18232951692@qq/com"
EMAIL_HOST_PASSWORD="123aoe"
DEFAUIL_FROM_EMAIL="3303236612@qq.com"#defauil
#celery#配置
import djcelery#导入django-celery模块
djcelery.setup_loader()#进行模块加载
BROKER_URL="redis://127.0.0.1:6379/1"#任务容器地址，redis数据库地址
CELERY_IMPORTS=('CeleryTask.tasks')#具体的任务文件
CELERY_TIMEZONE='Asia/Shanghai'#celery时区
CELERYBEAT_SCHEDULER='djcelery.schedulers.DatabaseScheduler'#celey处理器，固定
#celery的定时器

#schedules时间表 安排schedules schdeules时间表 安排；celery定时任务用到的包celery celery
from celery.schedules import timedelta#timedelta时间间隔timedelta  timedelta时间间隔timedelta
CELERYBEAT_SCHEDULE={#定时器策略
    #定时任务一：每隔30s运行一次
    u'测试定时器1':{
        "task":"CeleryTask.tasks.taskExample",
        #"schedule"crontab(minute='*/2’),#or 'schedule': timedelta(seconds=3)
        "schedule":timedelta(seconds=3),#3秒运行一次
        "args":(),
    },
    u'来自天主的问候':{
        "task":"CeleryTask.tasks.DingTalk",#文件位置
        "schedule":timedelta(seconds=3),#定时器，每3秒运行一次
        "args":(),
    },
}

#缓存配置
# CACHES={
#     'default':{
#         'BACKEND':'django.core.cache.backends.memcached.MemcachedCache',
#         #申明使用memcache进行缓存
#         'LOCATION':[
#         '127.0.0.1:11211'#缓存默认端口
#             ]#memcache地址
#     }
# }
# CACHES={
#     'default':{
#         'BACKEND':'django.core.cache.backends.locmem.LocMemCache'
#         #默认使用本地缓存
#     }
# }
# CACHES={
#     'default':{
#         'BACKEND':'django_redis.cache.RedisCache',
#         'LOCATION':[
#             'redis://127.0.0.1:6379/1'
#         ],#memcacha地址
#         'OPTIONS':{
#             'CLIENT_CLASS':'django_redis.client.DefaultClient'
#         }
#     }
# }
#

# CACHE_MIDDLEWARE_KEY_PREFIX=''
# CACHE_MIDDLEWARE_SECONDS=600#全局缓存的寿命
#数据库缓存
CACHES={
    'default':{
        'BACKEND':'django.core.cache.backends.db.DatabaseCache',
        #默认使用数据库缓存
        'LOCATION':'cache_table'#存放缓存的表
    }
}







