[![Coverage Status](https://coveralls.io/repos/github/brechin/django-computed-property/badge.svg?branch=master)](https://coveralls.io/github/brechin/django-computed-property?branch=master)
[![Build Status](https://travis-ci.org/brechin/django-computed-property.svg?branch=master)](https://travis-ci.org/brechin/django-computed-property)
# django-computed-property
Computed Property Fields for Django

Inspired by [Google Cloud Datastore NDB Computed Properties](https://cloud.google.com/appengine/docs/standard/python/ndb/entity-property-reference#computed).

Automatically store a computed value in the database when saving your model so you can filter
on values requiring complex (or simple!) calculations.

## Quick start

1. Install this library

    pip install django-computed-property
    
1. Add to `INSTALLED_APPS`
    
    INSTALLED_APPS = [
        ...,
        'computed_property'
    ]

Documentation available at http://django-computed-property.readthedocs.io/en/latest/
