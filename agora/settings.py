"""
Django settings for agora project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import logging
import accounts
from os import path
import saml2
from saml2.saml import NAMEID_FORMAT_PERSISTENT
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'secret-key'

# SECURITY WARNING don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1',
                 'localhost',
                 'agora-dev.vi-seem.eu',
                 'agora-dev.aris.grnet.gr',
                 'snf-708131.vm.okeanos.grnet.gr',
                 'spmt.eudat.eu',
                 'sp.eudat.eu',
                 'snf-715140.vm.okeanos.grnet.gr',
                 'snf-714484.vm.okeanos.grnet.gr',
                 'services.vi-seem.eu']


# CORS_ORIGIN_ALLOW_ALL = True

# Application definition

INSTALLED_APPS = [
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_jenkins',
    # 'social.apps.django_app.default',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'rest_framework',
    'corsheaders',
    'reversion',
    'component',
    'options',
    'owner',
    'service',
    'accounts',
    'djangosaml2'
]

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Agora Write Beta 1.0',
    'HEADER_DATE_FORMAT': 'l, j. F Y',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    'SHOW_REQUIRED_ASTERISK': True,  # Default True
    'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    'SEARCH_URL': '/admin/auth/user/',
    'MENU_ICONS': {
       'service': 'icon-leaf',
       'component': 'icon-leaf',
       'owner': 'icon-leaf',
       'sites': 'icon-leaf',
       'auth': 'icon-lock',
    },
    'MENU_OPEN_FIRST_CHILD': True, # Default True
    'MENU_EXCLUDE': ('auth.group',),
    'MENU': (
       'service',
       'component',
       'owner',
       'options',
       'sites',
    ),

    # misc
    'LIST_PER_PAGE': 15
 }

AUTH_USER_MODEL = "accounts.User"

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

LOGIN_URL= '/saml2/login/'

LOGIN_REDIRECT_URL = "/api/admin/"

PROJECT_APPS = ['component', 'options', 'owner', 'service']

SITE_ID = 1

SAML_ATTRIBUTE_MAPPING = {
    'mail': ('email', ),
    'givenName': ('first_name', ),
    'sn': ('last_name', ),
}

SAML_DJANGO_USER_MAIN_ATTRIBUTE = 'email'

SAML_CONFIG = {
  'xmlsec_binary': '/usr/bin/xmlsec1',
  'entityid': 'http://'+ALLOWED_HOSTS[SITE_ID]+'/saml2/metadata/',
  'attribute_map_dir': path.join(BASE_DIR, 'attribute-maps'),
  'service': {
        'sp' : {
                  'name': 'Agora Dev Service',
                  'name_id_format': NAMEID_FORMAT_PERSISTENT,
                  'authn_requests_signed': True,
                  "allow_unsolicited": True,
                  'endpoints': {
                                'assertion_consumer_service': [ ('http://'+ALLOWED_HOSTS[SITE_ID]+'/saml2/acs/',saml2.BINDING_HTTP_POST),  ],

                                'single_logout_service': [ ('http://'+ALLOWED_HOSTS[SITE_ID]+'/saml2/ls/',saml2.BINDING_HTTP_REDIRECT),
                                                         ('http://'+ALLOWED_HOSTS[SITE_ID]+'/saml2/ls/post',saml2.BINDING_HTTP_POST),  ],
                                },
                  'required_attributes': ['uid'],
                  'optional_attributes': ['mail','givenName', 'sn'],

                  'idp': {
                          # the keys of this dictionary are entity ids
                          'https://aai.vi-seem.eu/proxy/saml2/idp/metadata.php': {
                              'single_sign_on_service': {
                                  saml2.BINDING_HTTP_REDIRECT: 'https://aai.vi-seem.eu/proxy/saml2/idp/SSOService.php',
                                  },
                              'single_logout_service': {
                                  saml2.BINDING_HTTP_REDIRECT: 'https://aai.vi-seem.eu/proxy/saml2/idp/SingleLogoutService.php',
                                  },
                              },
                          },
        }
    },
         'key_file' : path.join(BASE_DIR, 'key.pem'),
         'cert_file' : path.join(BASE_DIR, 'cert.pem'),

        'metadata': {
              'local': [path.join(BASE_DIR, 'idp-metadata.xml')],
                },
        'debug': 1,
}



MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]




REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
      'EXCEPTION_HANDLER': 'agora.views.custom_exception_handler'}

ROOT_URLCONF = 'agora.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'agora.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
       'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'agora',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
    }
}

AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'djangosaml2.backends.Saml2Backend',)

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
CLIENT_ID = ''
APPLICATION_NAME = 'API-Client'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''

AVATAR_LOCATION = '/var/www/html/agora/static/img/avatars/'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',  # <--- enable this one
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'accounts.views.save_avatar'
)


MEDIA_ROOT = '/var/www/html/agora/static/img'

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/API-Client

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

STATICFILES_DIRS = (
   os.path.join(BASE_DIR, "static", "admin"),
   os.path.join(BASE_DIR, "static", "rest_framework_swagger"),
)


SWAGGER_SETTINGS = {
    'exclude_namespaces': [],
    'api_version': '1.0',
    'api_path': str(ALLOWED_HOSTS[SITE_ID])+'/api',
    'enabled_methods': [
        'get',
        'post',
        'put',
        'patch',
        'delete'
    ],
    'host': 'str(ALLOWED_HOSTS[SITE_ID])',
     'info': {
        'contact': 'admin@agora.com',
        'description': 'This is a demonstration of the API documentation engine. '
                       'The full Git repository is availible at <a href="https://code.vi-seem.eu/stdario/agora">'
                       'Agora Git</a> where the current development version is availible in the DEV branch.'
                       'The current stable version is availible at the MASTER branch.',
        'license': 'Apache 2.0',
        'licenseUrl': 'http://www.apache.org/licenses/LICENSE-2.0.html',
        'termsOfServiceUrl': '/',
        'title': 'Agora API v1.0',
    },
    'api_key': '',
    'is_authenticated': False,
    'is_superuser': False,
    'permission_denied_handler': None,
    'resource_access_handler': None,
    'base_path':str(ALLOWED_HOSTS[SITE_ID])+'/api/docs',
    'doc_expansion': 'list',
    'operationsSorter' : 'method'

}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/www/html/agora/logs/debug.log',
        },

    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


