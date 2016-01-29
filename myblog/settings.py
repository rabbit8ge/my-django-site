"""
Django settings for myblog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import django.conf.global_settings as DEFAULT_SETTINGS
from django.conf.global_settings import DATABASES, DEBUG,\
    FILE_UPLOAD_MAX_MEMORY_SIZE, DEFAULT_FILE_STORAGE, STATICFILES_DIRS
    
try:
    print(os.listdir('/usr/local/sae/python/lib/python2.7/site-packages'))
except:
    print('debug: cant see')
try:
    print(os.listdir('/usr/local/sae/python/lib/python2.7/site-packages/sae'))
except:
    print('debug: cant see')

print('debug: start settings.')

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a%=kr#y@1#a1x7c7h!_f2o4@p+4p@$-jw1muw89e6yyx3hibdu'

# Application definition
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'pipeline.finders.PipelineFinder',
)

INSTALLED_APPS = (
    'wpadmin', # before django.contrib.admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'blogs',
    'tagging',
    'pipeline',
    'django.contrib.sitemaps',
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.cssmin.CSSMinCompressor'
PIPELINE_CSSMIN_BINARY = 'cssmin'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.slimit.SlimItCompressor'
PIPELINE_ENABLED = True

PIPELINE_CSS = {
    'style': {
        'source_filenames': (
            'assets/css/normalize.css',
            'assets/font/font-awesome/css/font-awesome.min.css',
            'assets/libs/materialize/css/materialize.min.css',
            'assets/css/bootstrap.css',
            'assets/css/animate.min.css',
            'assets/libs/sweetalert/sweet-alert.css',
            'assets/libs/owl-carousel/owl.carousel.css',
            'assets/libs/owl-carousel/owl.transitions.css',
            'assets/libs/owl-carousel/owl.theme.css',
            'assets/css/main.css',
            'assets/css/responsive.css',
            'assets/css/colors/color1.css',
        ),
        'output_filename': 'global.css',
        'variant' : 'datauri',
    },
    'style2': {
        'source_filenames': (
            'assets/css/normalize.css',
            'assets/font/font-awesome/css/font-awesome.min.css',
            'assets/libs/materialize/css/materialize.min.css',
            'assets/css/bootstrap.css',
            'assets/css/animate.min.css',
            'assets/libs/sweetalert/sweet-alert.css',
            'assets/libs/owl-carousel/owl.carousel.css',
            'assets/libs/owl-carousel/owl.transitions.css',
            'assets/libs/owl-carousel/owl.theme.css',
            'assets/css/main.css',
            'assets/css/responsive.css',
            'assets/css/colors/color1.css',
            'assets/css/blog.css',
        ),
        'output_filename': 'global2.css',
        'variant' : 'datauri',
    }
}

PIPELINE_JS = {
    'scripts': {
        'source_filenames': (
            'assets/js/jquery.easing.1.3.js',
            'assets/js/detectmobilebrowser.js',
            'assets/js/isotope.pkgd.min.js',
            'assets/js/wow.min.js',
            'assets/js/waypoints.js',
            'assets/js/jquery.counterup.min.js',
            'assets/js/jquery.nicescroll.min.js',
            'assets/js/gmaps.js',
            'assets/libs/owl-carousel/owl.carousel.min.js',
            'assets/libs/materialize/js/materialize.min.js',
            'assets/libs/jwplayer/jwplayer.js',
            'assets/libs/sweetalert/sweet-alert.min.js',
            'assets/js/common.js',
            'assets/js/main.js',
            'assets/js/rrssb.js',

        ),
        'output_filename': 'scripts.js',
        'variant' : 'datauri',
    }
}


MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
)

ROOT_URLCONF = 'myblog.urls'

WSGI_APPLICATION = 'myblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
'''DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'app_heyiping',
         'USER': 'root',
         'PASSWORD': '',
         'HOST': '',
         'PORT': '',
     }
 }'''
 
ACCESSKEY = 'ooy5ylmz3y'
SECRETKEY = 'ml1j30mi5kk12m35ji14i2ljxx51l1ylh0x3lkjl'
if True:#'SERVER_SOFTWARE' in os.environ:
    # see: http://www.sinacloud.com/doc/sae/python/faq.html#id6
    # For SAE configuration.
    print 'debug: server mode'
    if 'COMPUTERNAME' in os.environ:
        from sae._restful_mysql import monkey
        monkey.patch()
    MYSQL_HOST = 'w.rdc.sae.sina.com.cn'
    MYSQL_PORT = '3307'
    MYSQL_USER = ACCESSKEY
    MYSQL_PASS = SECRETKEY
    MYSQL_DB = 'app_heyiping'
else:
    print 'debug: local mode'
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = ''
    MYSQL_USER = 'root'
    MYSQL_PASS = ''
    MYSQL_DB = 'app_heyiping'

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': MYSQL_DB,
         'USER': MYSQL_USER,
         'PASSWORD': MYSQL_PASS,
         'HOST': MYSQL_HOST,
         'PORT': MYSQL_PORT,
     }
 }

# SAE related configurations. see http://www.sinacloud.com/doc/sae/python/tutorial.html
STORAGE_BUCKET_NAME = 'media' # must defined before importing STORAGE_BUCKET_NAME
from sae.ext.django.storage.backend import STORAGE_BUCKET_NAME
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760
DEFAULT_FILE_STORAGE = 'sae.ext.django.storage.backend.Storage'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
#STATIC_ROOT = 'e:/workspace/sae/mysite/static_files/'
#STATIC_ROOT = os.path.join(os.path.dirname(__file__),'..','static_files').replace('\\','/') # static files will be generated in this folder with command manage.py collectstatic
#STATIC_ROOT = 'E:/workspace/sae/heyiping/static_files/'
STATIC_ROOT = 'static/' # Modify to static before uploading to SAE.
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'
DOCS_ROOT = 'docs/'

#STATICFILES_DIRS = ()
#STATICFILES_DIRS = os.path.join(
#    os.path.dirname(__file__), '..', 'static').replace('\\', '/'),
#STATICFILES_DIRS = (STATIC_ROOT.replace('\\', '/'), ) # see: http://www.ziqiangxuetang.com/django/django-static-files.html
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), '..', 'templates').replace('\\', '/'),)
'''CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'unix:/tmp/memcached.sock',
        'TIMEOUT': 60,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}'''

CKEDITOR_UPLOAD_PATH = "editor_uploads/"
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'cms',
        'height': 500,
        'width': 1050,
        'skin': 'moono',
        'extraPlugins': 'syntaxhighlight,youtube',

    },
}

WPADMIN = {
    'admin': {

        'title': 'He Yiping',
        'menu': {
            'top': 'wpadmin.menu.menus.BasicTopMenu',
            'left': 'wpadmin.menu.menus.BasicLeftMenu',
        },
        'dashboard': {
            'breadcrumbs': True,
        },
        'custom_style': STATIC_URL + 'wpadmin/css/themes/midnight.css',
    }
}

try:
    from local_settings import *
except ImportError:
    pass
try:
    from production_settings import *
except ImportError:
    pass

ALLOWED_HOSTS = ['*']

DEBUG = False

# define this variable in order to write/read file in python.
# you can use the command to import the variable.
# from django.conf.settings import PROJECT_ROOT
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__)+"/..")
print(PROJECT_ROOT)

print('debug: end settings')
