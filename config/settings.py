import os
import pymysql
pymysql.install_as_MySQLdb()


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = '$ty&gm8t*9(mslr$b-kz44%12f8@(&ocf8bpg1!1*o#_$(7px3'


DEBUG = True

ALLOWED_HOSTS = []



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'onlineshop',
        'USER': 'dnjsrb0710',
        'PASSWORD': 'mike7100',
        'HOST': 'onlineshop.cuiqfmmupoqp.ap-northeast-2.rds.amazonaws.com',
        'PORT': '3306'
    }
}



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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



AWS_ACCESS_KEY_ID='AKIAU5UAW4M6C2ZFFV4X'
AWS_SECRET_ACCESS_KEY='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'
AWS_REGION='ap-northeast-2'
AWS_STORAGE_BUCKET_NAME='wongueonlineshop'
AWS_S3_CUSTOM_DOMAIN='%s.s3.%s.amazonaws.com'%(AWS_STORAGE_BUCKET_NAME,AWS_REGION)
AWS_S3_OBJECT_PARAMETERS={
    'CacheControl':'max-age=86400',
}
AWS_DEFAULT_ACL='public-read'
AWS_LOCATION='static'


STATIC_URL = 'https://%s/%s/'%(AWS_S3_CUSTOM_DOMAIN,AWS_LOCATION)
STATICFILES_STORAGE='storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE='config.asset_storage.MediaStorage'


