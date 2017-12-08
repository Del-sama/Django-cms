# Define development specific settings
import json
import os
import sys
from dotenv import load_dotenv
from os.path import join, dirname

from .base import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load .env variables with python-dotenv
dotenv_path = join(BASE_DIR, '.env')
load_dotenv(dotenv_path)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

with open("{}/config.json".format(BASE_DIR)) as f:
    config = json.load(f)
    print(config)


if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'test.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'cms_api',
            'USER': config['USER'],
            'PASSWORD': config["PASSWORD"],
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    },
 }
 