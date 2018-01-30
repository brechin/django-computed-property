[![Coverage Status](https://coveralls.io/repos/github/brechin/django-computed-property/badge.svg?branch=master)](https://coveralls.io/github/brechin/django-computed-property?branch=master)
[![Build Status](https://travis-ci.org/brechin/django-computed-property.svg?branch=master)](https://travis-ci.org/brechin/django-computed-property)
# django-computed-property
Computed Property Fields for Django

Inspired by [Google Cloud Datastore NDB Computed Properties](https://cloud.google.com/appengine/docs/standard/python/ndb/entity-property-reference#computed).

Automatically store a computed value in the database when saving your model so you can filter
on values requiring complex (or simple!) calculations.

## Quick start

1. Install this library

    ```
    pip install django-computed-property
    ```
    
1. Add to `INSTALLED_APPS`
    
    ```python
    INSTALLED_APPS = [
        ...,
        'computed_property'
    ]
    ```

1. Add a computed field to your model(s)

    ```python
    from django.db import models
    import computed_property
 
    class MyModel(models.model):
        doubled = computed_property.ComputedIntegerField(compute_from='double_it')
        base = models.IntegerField()
     
        def double_it(self):
            return self.base * 2
    ```

Documentation available at http://django-computed-property.readthedocs.io/en/latest/
