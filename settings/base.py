"""
Django settings for drugzone project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'iz2fz2=aq4(ae$%hfg67w=v_3wm3=4xm$rj#0)pp8tj9u5w6yx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # APIS APP
    'drugZoneUsers.apps.DrugzoneusersConfig',

   
    'rest_framework',
    'rest_framework.authtoken',


    # Dashboard Apps

    'DashBoard',
    'UserJourney',
    'LabAdmin',
    'CategoryAndSubcategory',
    'Medicines',
    'doctorConsultation',
    'prescription'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrsfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'settings.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_drugzone1',
        'USER': 'tarjeet',
        'PASSWORD': 'admin',
        'HOST':'localhost',
        'PORT':''
        # 'OPTIONS': {
        # "init_command": "SET foreign_key_checks = 0;", 
        # }

}
    
}


AUTH_USER_MODEL = 'drugZoneUsers.CustomUser'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    # 'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)

   
    
}
    
# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

JET_DEFAULT_THEME = 'green'
# JET_THEMES = [
#     # {
#     #     'theme': 'default', # theme folder name
#     #     'color': '#47bac1', # color of the theme's button in user menu
#     #     'title': 'Default' # theme title
#     # },
#     {
#         'theme': 'green',
#         'color': '#44b78b',
#         'title': 'Green'
#     },
#     # {
#     #     'theme': 'light-green',
#     #     'color': '#2faa60',
#     #     'title': 'Light Green'
#     # },
#     # {
#     #     'theme': 'light-violet',
#     #     'color': '#a464c4',
#     #     'title': 'Light Violet'
#     # },
#     # {
#     #     'theme': 'light-blue',
#     #     'color': '#5EADDE',
#     #     'title': 'Light Blue'
#     # },
#     # {
#     #     'theme': 'light-gray',
#     #     'color': '#222',
#     #     'title': 'Light Gray'
#     # }
# ]


# CORS_ALLOW_HEADERS = (
#         'x-requested-with',
#         'content-type',
#         'accept',
#         'accept-encoding',
#         'dnt',
#         'user-agent',
#         'origin',
#         'authorization',
#         'x-csrftoken'
#     )


# CORS_ALLOW_CREDENTIALS = True
# CORS_ORIGIN_ALLOW_ALL = True
