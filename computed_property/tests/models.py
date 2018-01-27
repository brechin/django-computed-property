import datetime
from django.db import models

import computed_property as fields


class ComputedText(models.Model):
    computed = fields.ComputedTextField(
        compute_from=lambda x: 'char has %s' % x.base_value
    )
    base_value = models.CharField(
        max_length=25,
        default='foo'
    )


class ComputedChar(models.Model):
    computed = fields.ComputedCharField(
        max_length=25,
        compute_from=lambda self: 'char has %s' % self.base_value
    )
    base_value = models.CharField(
        max_length=25,
        default='foo'
    )


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


class ComputedInt(models.Model):
    computed = fields.ComputedIntegerField(
        compute_from='compute_val'
    )
    base_value = models.IntegerField(
        default=123
    )

    @property
    def compute_val(self):
        return self.base_value + 1000


class ComputedDate(models.Model):
    computed = fields.ComputedDateField(
        compute_from='base_value'
    )
    base_value = models.DateField()


class ComputedDateTime(models.Model):
    computed = fields.ComputedDateTimeField(
        compute_from=lambda self: self.base_value + datetime.timedelta(days=1)
    )
    base_value = models.DateTimeField()


class ComputedNullable(models.Model):
    computed = fields.ComputedIntegerField(
        null=True,
        compute_from=lambda x: None
    )
