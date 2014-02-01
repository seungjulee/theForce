"""
Django settings for theForce project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


PROJECT_DIRECTORY = os.path.realpath(os.path.dirname(__file__)) + '/../'
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIRECTORY,'templates/'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j)^lc#7ihpdzv5+2&^gmx41+&^)xy+1!73@2qst5mww(cio)uy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'salesforce',
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'theForce.urls'

WSGI_APPLICATION = 'theForce.wsgi.application'

#Email Servers
EMAIL_USE_TLS = True

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = 'duzhangtech@gmail.com'

EMAIL_HOST_PASSWORD = 'Starcraft2'

EMAIL_PORT = 587


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {

#   'default': {
#       'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#       'NAME': 'first',                      # Or path to database file if using sqlite3.
#       'USER': 'root',                  # Not used with sqlite3.
#       'PASSWORD': 'Starcraft2',                   # Not used with sqlite3.
#       'HOST': 'localhost',                # Set to empty string for localhost. Not used with sqlite3.
#       'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
#    }

'default':{
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'mydb',
},

'salesforce':{
    'ENGINE': 'salesforce.backend',
    "CONSUMER_KEY" : '3MVG9A2kN3Bn17huXp3x6eQ5zPXCdEHZCt.clSy1TyK0yJbDV_8H1wn.dfAa_d60qyvihVgtiXVdgkwensNG9',
    "CONSUMER_SECRET" : '7783134933470171276',
    'USER': 'duzhangtech',
    'PASSWORD': 'Starcraft2',
    'HOST': 'https://test.salesforce.com',
}

}
DATABASE_ROUTERS = [
    "salesforce.router.ModelRouter"
    ]
SALESFORCE_DB_ALIAS = 'salesforce'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = ''

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
# Additional locations of static files

STATICFILES_DIRS = (
    PROJECT_DIRECTORY + 'static/',
#     # Put strings here, like "/home/html/static" or "C:/www/django/static".
#     # Always use forward slashes, even on Windows.
#     # Don't forget to use absolute paths, not relative paths.
)

# # List of finder classes that know how to find static files in
# # various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

#email loggin
AUTHENTICATION_BACKENDS = ('backends.EmailAuthBackend',)