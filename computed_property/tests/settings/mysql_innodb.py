from .base import *  # noqa

import os

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, 'testdb.mysql_innodb')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_computed_property{}'.format(db_suffix),  # noqa
        'HOST': '127.0.0.1',
        'PORT': 12345,
        'USER': 'root',
        'OPTIONS': {'init_command': 'SET default_storage_engine=InnoDB'},
    }
}
