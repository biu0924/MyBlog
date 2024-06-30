import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR: 项目根目录的路径，
# 一般使用 Path(__file__).resolve().parent.parent 获取。
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY: 项目的密钥，用于提供加密签名等。应保持秘密，不要公开
SECRET_KEY = 'django-insecure-pdpa+hz0%w^1_ha0m7%*b5u0b35_*xgwhml-(no3y_sw3gia%s'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG: 调试模式开关。开发阶段设置为 True，生产环境应设置为 False
DEBUG = True

# ALLOWED_HOSTS: 允许访问的主机名列表。在生产环境中，应列出你的域名或IP地址。
ALLOWED_HOSTS = []


# Application definition
# INSTALLED_APPS: 已安装的Django应用程序列表。
# 包括Django自带的应用和你自己创建的应用。
INSTALLED_APPS = [
    'django.contrib.admin',# 管理员站点
    'django.contrib.auth',# 认证授权系统
    'django.contrib.contenttypes',# 内容类型框架
    'django.contrib.sessions',# 会话框架
    'django.contrib.messages',# 消息框架
    'django.contrib.staticfiles',# 管理静态文件框架
    # 以上自带的，下面是自己的
    'blog.apps.BlogConfig',
]
'''
python manage.py migrate
    这个 migrate 命令查看 INSTALLED_APPS 配置，
    并根据 mysite/settings.py 文件中的数据库配置和随应用提供的数据库迁移文件（我们将在后面介绍这些），
    创建任何必要的数据库表。你会看到它应用的每一个迁移都有一个消息。如果你有兴趣，
    运行你的数据库的命令行客户端，
    输入 \dt （PostgreSQL）， SHOW TABLES; （MariaDB，MySQL）， .tables （SQLite）
    或 SELECT TABLE_NAME FROM USER_TABLES; （Oracle）来显示 Django 创建的表。
'''
# # 告诉Django使用你自定义的用户模型
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
# 设置会话引擎为Cookie
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

# MIDDLEWARE: 中间件列表。中间件是在请求和响应过程中执行的钩子
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 以上是自带的
    'blog.middleware.DefaultLoginMiddleware',
]

# ROOT_URLCONF: 根URL配置模块的路径。通常是项目目录下的 urls.py 文件。
ROOT_URLCONF = 'myblog.urls'

# TEMPLATES: 模板引擎配置，定义如何加载和渲染模板。
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'blog'/'templates'],
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

# WSGI_APPLICATION: WSGI应用程序的路径。用于部署。
WSGI_APPLICATION = 'myblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
# DATABASES: 数据库配置。定义数据库引擎、名称、用户、密码、主机和端口
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog',  # 替换为你的数据库名
        'USER': 'root',  # 替换为你的数据库用户名
        'PASSWORD': '123456',  # 替换为你的数据库密码
        'HOST': 'localhost',  # 如果 MySQL 运行在本地，使用 'localhost'
        'PORT': '3306',  # MySQL 默认端口是 3306
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
# AUTH_PASSWORD_VALIDATORS: 密码验证器列表，用于验证用户密码的强度
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
# https://docs.djangoproject.com/en/5.0/topics/i18n/
# LANGUAGE_CODE: 项目的默认语言代码
LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE: 项目的默认时区。
TIME_ZONE = 'Asia/Shanghai'

# USE_I18N: 是否启用国际化支持。
# USE_L10N: 是否启用本地化支持。
USE_I18N = True

# USE_TZ: 是否启用时区支持。
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
# STATIC_URL: 静态文件的URL。
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR /"static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
# DEFAULT_AUTO_FIELD: 默认的自动字段类型，通常是 BigAutoField
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'blog/media')
