import datetime

from decimal import Decimal
from django.db import models

import computed_property as fields


def always_true(_):  # Needs to consume an arg
    return True


class ComputedBool(models.Model):
    computed = fields.ComputedBooleanField(compute_from=always_true)
    base_value = models.BooleanField(default=False)


class ComputedChar(models.Model):
    computed = fields.ComputedCharField(
        max_length=25,
        compute_from=lambda self: 'char has %s' % self.base_value
    )
    base_value = models.CharField(
        max_length=25,
        default='foo'
    )


class ComputedDate(models.Model):
    computed = fields.ComputedDateField(
        compute_from='base_value'
    )
    base_value = models.DateField()


class ComputedDateFromDateTime(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    computed = fields.ComputedDateField(
        compute_from='created_at'
    )


class ComputedDateTime(models.Model):
    computed = fields.ComputedDateTimeField(
        compute_from=lambda self: self.base_value + datetime.timedelta(days=1)
    )
    base_value = models.DateTimeField()


class ComputedDecimal(models.Model):
    computed = fields.ComputedDecimalField(compute_from='convert_to_decimal',
                                           max_digits=3,
                                           decimal_places=2)
    base_value = models.IntegerField(default=100)

    def convert_to_decimal(self):
        return Decimal(self.base_value) / Decimal('100.0')


class ComputedEmail(models.Model):
    computed = fields.ComputedEmailField(
        compute_from='prepend_test_to_email'
    )
    base_value = models.EmailField(
        max_length=25,
        default='foo@example.com'
    )

    def prepend_test_to_email(self):
        return 'test%s' % self.base_value


class ComputedFloat(models.Model):
    computed = fields.ComputedFloatField(compute_from='convert_to_float')
    base_value = models.IntegerField(default=100)

    def convert_to_float(self):
        return float(self.base_value / 100.0)


class AbstractInt(models.Model):
    base_value = models.IntegerField(
        default=123
    )

    @property
    def compute_val(self):
        return self.base_value + 1000

    class Meta:
        abstract = True


class ComputedInt(AbstractInt):
    computed = fields.ComputedIntegerField(
        compute_from='compute_val'
    )


class ComputedNullable(models.Model):
    computed = fields.ComputedIntegerField(
        null=True,
        compute_from=lambda x: None
    )


class ComputedPositiveInt(AbstractInt):
    computed = fields.ComputedPositiveIntegerField(compute_from='compute_val')


class ComputedPositiveSmallInt(AbstractInt):
    computed = fields.ComputedPositiveSmallIntegerField(
        compute_from='compute_val'
    )


class ComputedSmallInt(AbstractInt):
    computed = fields.ComputedSmallIntegerField(compute_from='compute_val')


class ComputedText(models.Model):
    computed = fields.ComputedTextField(
        compute_from=lambda x: 'char has %s' % x.base_value
    )
    base_value = models.CharField(
        max_length=25,
        default='foo'
    )


class ComputedTime(models.Model):
    computed = fields.ComputedTimeField(compute_from='base_value')
    base_value = models.DateTimeField()
