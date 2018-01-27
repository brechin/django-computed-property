Welcome to django-computed-property!
====================================================

Computed Property fields for Django models, inspired by `Google Cloud NDB`_

.. _Google Cloud NDB: https://cloud.google.com/appengine/docs/standard/python/ndb/entity-property-reference#computed


Prerequisites
-------------

``django-computed-property`` supports `Django`_ 1.8 - 2.0 on Python 2.7, 3.3,
3.4, 3.5, 3.6, pypy, and pypy3.

Only SQLite is tested, but any Django database backend should work.

.. _Django: http://www.djangoproject.com/


Installation
------------

``django-computed-property`` is available on `PyPI`_. Install it with::

    pip install django-computed-property

.. _PyPI: https://pypi.python.org/pypi/django-computed-property/


Usage
-----

Just import and use the included field classes in your models::

    from django.db import models
    from computed_property import ComputedTextField


    class MyModel(models.Model):
        name = ComputedTextField(compute_from='calculation')

        @property
        def calculation(self):
            return 'some complicated stuff'

You can read values from the ``name`` field as usual, but you may not set the field's value.
When the field is accessed and when a model instance is saved, it will compute the field's value
using the provided callable (function/lambda), property name, or attribute name.


Field types
~~~~~~~~~~~

Several other field classes are included: ``ComputedCharField``,
``ComputedEmailField``, ``ComputedIntegerField``, ``ComputedDateField``, and
``ComputedDateTimeField``. All field classes accept the same arguments as
their non-Computed versions.

To create an Computed version of some other custom field class, inherit from
both ``ComputedField`` and the other field class::

    from computed_property import ComputedField
    from somewhere import MyField

    class MyComputedField(ComputedField, MyField):
        pass


Contributing
------------

See the `contributing docs`_.

.. _contributing docs: https://github.com/orcasgit/django-computed-property/blob/master/CONTRIBUTING.rst