import tempfile

from .base import *  # noqa

import os

HERE = os.path.dirname(os.path.abspath(__file__))
_fd, db_filename = tempfile.mkstemp(prefix="test_")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': db_filename,
        'TEST': {'NAME': db_filename},
    },
}
