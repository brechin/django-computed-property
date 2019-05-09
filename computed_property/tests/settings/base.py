import os


INSTALLED_APPS = [
    'computed_property.tests',
]

SECRET_KEY = 'secret'
SILENCED_SYSTEM_CHECKS = ['1_7.W001']

# Used to construct unique test database names to allow detox to run multiple
# versions at the same time
db_suffix = "_%s" % os.getuid()
