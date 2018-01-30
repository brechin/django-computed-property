from __future__ import print_function

from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.db.models.signals import pre_save

__all__ = [
    'ComputedBooleanField',
    'ComputedCharField',
    'ComputedDateField',
    'ComputedDateTimeField',
    'ComputedDecimalField',
    'ComputedEmailField',
    'ComputedField',
    'ComputedFloatField',
    'ComputedIntegerField',
    'ComputedPositiveIntegerField',
    'ComputedPositiveSmallIntegerField',
    'ComputedSmallIntegerField',
    'ComputedTextField',
    'ComputedTimeField',
]


class ComputedField(models.Field):
    def __init__(self, compute_from=None, *args, **kwargs):
        kwargs['editable'] = False
        if compute_from is None:
            raise ImproperlyConfigured(
                '%s requires setting compute_from' %
                self.__class__.__name__
            )
        super(ComputedField, self).__init__(*args, **kwargs)
        self.compute_from = compute_from

    class ObjectProxy(object):
        def __init__(self, field):
            self.field = field

        def __get__(self, instance, cls=None):
            if instance is None:
                return self
            value = self.field.calculate_value(instance)
            instance.__dict__[self.field.name] = value
            return value

        def __set__(self, obj, value):
            pass

    def contribute_to_class(self, cls, name, **kwargs):
        """Add field to class using ObjectProxy so that
        calculate_value can access the model instance."""
        self.set_attributes_from_name(name)
        cls._meta.add_field(self)
        self.model = cls
        setattr(cls, name, ComputedField.ObjectProxy(self))
        pre_save.connect(self.resolve_computed_field, sender=cls)

    def resolve_computed_field(self, sender, instance, raw, **kwargs):
        """Pre-save signal receiver to compute new field value."""
        setattr(instance, self.get_attname(), self.calculate_value(instance))
        return self.calculate_value(instance)

    def calculate_value(self, instance):
        """
        Retrieve or call function to obtain value for this field.
        Args:
            instance: Parent model instance to reference
        """
        if callable(self.compute_from):
            value = self.compute_from(instance)
        else:
            instance_compute_object = getattr(instance, self.compute_from)
            if callable(instance_compute_object):
                value = instance_compute_object()
            else:
                value = instance_compute_object
        return self.to_python(value)

    def deconstruct(self):
        name, path, args, kwargs = super(ComputedField, self).deconstruct()
        kwargs['compute_from'] = self.compute_from
        return name, path, args, kwargs

    def to_python(self, value):
        return super(ComputedField, self).to_python(value)

    def get_prep_value(self, value):
        return super(ComputedField, self).get_prep_value(value)


class ComputedBooleanField(ComputedField, models.BooleanField):
    pass


class ComputedCharField(ComputedField, models.CharField):
    pass


class ComputedDateField(ComputedField, models.DateField):
    pass


class ComputedDateTimeField(ComputedField, models.DateTimeField):
    pass


class ComputedDecimalField(ComputedField, models.DecimalField):
    pass


class ComputedEmailField(ComputedField, models.EmailField):
    pass


class ComputedFloatField(ComputedField, models.FloatField):
    pass


class ComputedIntegerField(ComputedField, models.IntegerField):
    pass


class ComputedPositiveIntegerField(ComputedField, models.PositiveIntegerField):
    pass


class ComputedPositiveSmallIntegerField(ComputedField,
                                        models.PositiveSmallIntegerField):
    pass


class ComputedSmallIntegerField(ComputedField, models.SmallIntegerField):
    pass


class ComputedTextField(ComputedField, models.TextField):
    pass


class ComputedTimeField(ComputedField, models.TimeField):
    pass
