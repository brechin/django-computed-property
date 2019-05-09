from .base import *  # noqa

import os
import platform


if platform.python_implementation().upper() == 'PYPY':
    from psycopg2cffi import compat
    compat.register()


HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, 'testdb.sqlite')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'travis_ci_test',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}
