Welcome to django-computed-property!
====================================================

Computed Property fields for Django models, inspired by `Google Cloud NDB`_

.. _Google Cloud NDB: https://cloud.google.com/appengine/docs/standard/python/ndb/entity-property-reference#computed


Prerequisites
-------------

``django-computed-property`` supports (i.e. is tested on) `Django`_ 1.8 - 2.2 and trunk on Python 2.7,
3.4, 3.5, 3.6, 3.7, pypy, and pypy3.

SQLite and Postgres are currently tested, but any Django database backend should work.

.. _Django: http://www.djangoproject.com/


Installation
------------

``django-computed-property`` is available on `PyPI`_. Install it with::

    pip install django-computed-property

.. _PyPI: https://pypi.python.org/pypi/django-computed-property/


Usage
-----

Add computed_property to your list of `INSTALLED_APPS` in `settings.py`::

    INSTALLED_APPS = [
        ...
        'computed_property'
    ]

Then, simply import and use the included field classes in your models::

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

`compute_from` can be a reference to a function that takes a single argument (an instance of the model), or
a string referring to a field, property, or other attribute on the instance.


.. note::

    It is important to note that your computed field data will not immediately be written to the database.
    You must (re-)save all instances of your data to have the computed fields populated in the database. Until
    you do so, you will be able to access those fields when you load an instance of the model, but
    you will not benefit from their queryability.

    One way you could do this is in a data migration, using something like::

        for instance in MyModel.objects.all().iterator():
            instance.save()


Field types
~~~~~~~~~~~

Several other field classes are included: ``ComputedCharField``,
``ComputedEmailField``, ``ComputedIntegerField``, ``ComputedDateField``,
``ComputedDateTimeField``, and others. All field classes accept the same arguments as
their non-Computed versions.

To create an Computed version of some other field class, inherit from
both ``ComputedField`` and the other field class::

    from computed_property import ComputedField
    from somewhere import MyField

    class MyComputedField(ComputedField, MyField):
        pass


Contributing
------------

See the `contributing docs`_.

.. _contributing docs: https://github.com/orcasgit/django-computed-property/blob/master/CONTRIBUTING.rst