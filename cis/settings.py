import os

env = os.environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "-^rq(x*d--6_#635*jdvfin@(-3(9vdr_s$9+^@cw1356q(ja"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
ALLOWED_HOSTS = ["*", "cis-django-dev.azurewebsites.net"]

# Application definition
# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # "django.contrib.humanize", # Handy template tags
    "django.contrib.admin",
    "django.forms",
]
THIRD_PARTY_APPS = [
    "crispy_forms",
    "django_celery_beat",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "oauth2_provider",
    "drf_yasg",
    "django_extensions",
]

LOCAL_APPS = [
    "emailscraper.apps.EmailscraperConfig",
    # Your stuff: custom apps go here
]
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "cis.middlewares.CsrfMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "cis.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "cis.wsgi.application"

# Database

DATABASES = {
    "default": {
        "ENGINE": "sql_server.pyodbc",
        "NAME": "cis_db",
        "HOST": "cis-app.database.windows.net",
        "USER": "cis-admin",
        "PASSWORD": "password123@",
        "OPTIONS": {
            "driver": "ODBC Driver 17 for SQL Server",
        },
    }
}

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = "/static/"
SITE_ID = 1

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
    )
}

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    "SCOPES": {"read": "Read scope", "write": "Write scope"},
    "ACCESS_TOKEN_EXPIRE_SECONDS": 3600,
}


LOG_DIR = BASE_DIR + "/logs"
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    # Formatters ####################################################################
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(name)s %(pathname)s %(funcName)s %(message)s"
        }
    },
    # Handlers ####################################################################
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "formatter": "verbose",
            "filename": LOG_DIR + "/log.log",
        },
        "questions": {
            "level": "INFO",
            "class": "logging.FileHandler",
            # 'class':'logging.handlers.RotatingFileHandler',
            # 'maxBytes': 1024 * 1024 * 10, #Max 10MB
            "formatter": "verbose",
            "filename": LOG_DIR + "/question.log",
            # 'backupCount' : 10,
        },
    },
    # Loggers ####################################################################
    "loggers": {
        "django": {"handlers": ["file"], "propagate": True, "level": "INFO"},
        "questions": {"level": "INFO", "propagate": True, "handlers": ["questions"]},
    },
}

STATIC_ROOT = os.path.join(BASE_DIR, "static")

# ENVIRONMENT VARS
SCRAPING_EMAIL = os.environ.get("SCRAPING_EMAIL", "duahimanshu100@outlook.com")
SCRAPING_PASSWORD = os.environ.get("SCRAPING_PASSWORD", "brics123@")
IMAP_HOST = os.environ.get("IMAP_HOST", "outlook.office365.com")
DATA_UNIT = "MB"
USER_NAME = "dbadmin"
FILTER_DOMAIN = 'FROM "@hotmail.com"'
FILTER_SUBJECT = 'SUBJECT "Summary report for network"'
# celery
CELERY_BROKER_URL = os.environ.get("REDIS_URL","redis://localhost:6379/0")
CELERY_RESULT_BACKEND =  os.environ.get("REDIS_URL","redis://localhost:6379/0")
CELERY_IMPORTS = ("emailscraper.tasks",)
