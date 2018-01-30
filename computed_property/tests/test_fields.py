from datetime import date, datetime, time
from decimal import Decimal

import pytest
from django.core.exceptions import ImproperlyConfigured

from computed_property import ComputedCharField, ComputedField
from . import models


@pytest.mark.parametrize(
    'model,vals',
    [  # Vals should be [base_value input, expected, 2nd non-matching input]
        (models.ComputedBool,
         [False, True]),  # Second input omitted because it doesn't make sense
        (models.ComputedChar,
         ['one', 'char has one', 'test']),
        (models.ComputedDate,
         [date(2015, 2, 5), date(2015, 2, 5), date(2019, 4, 1)]),
        (models.ComputedDateTime,
         [datetime(2015, 2, 5, 15),
          datetime(2015, 2, 6, 15),
          datetime(2015, 4, 1, 15)],),
        (models.ComputedDecimal,
         [123, Decimal('1.23'), 456]),
        (models.ComputedEmail,
         ['a@example.com', 'testa@example.com', 'garbage@example.com']),
        (models.ComputedFloat,
         [123, float(1.23), 456]),
        (models.ComputedInt,
         [1, 1001, 9999]),
        (models.ComputedPositiveInt,
         [1, 1001, 9999]),
        (models.ComputedPositiveSmallInt,
         [1, 1001, 9999]),
        (models.ComputedSmallInt,
         [1, 1001, 9999]),
        (models.ComputedText,
         ['baz', 'char has baz', 'test']),
        (models.ComputedTime,
         [datetime(2018, 4, 1, 14, 13, 12),
          time(14, 13, 12),
          datetime(2018, 1, 2, 3, 4, 5)])
    ],

)
class TestBasicFunctionality(object):
    def test_create(self, db, model, vals):
        created = model.objects.create(base_value=vals[0])
        assert vals[1] == created.computed

    def test_search(self, db, model, vals):
        created = model.objects.create(base_value=vals[0])
        fetched = model.objects.get(computed=vals[1])
        assert created == fetched
        assert created.id == fetched.id

    def test_save_modification(self, db, model, vals):
        if len(vals) < 3:
            return
        created = model.objects.create(base_value=vals[2])
        assert vals[1] != created.computed
        created.base_value = vals[0]
        created.save()
        assert vals[1] == created.computed

    def test_live_modification(self, db, model, vals):
        if len(vals) < 3:
            return
        created = model.objects.create(base_value=vals[2])
        assert vals[1] != created.computed
        created.base_value = vals[0]
        assert vals[1] == created.computed

    def test_access_field(self, db, model, vals):
        assert isinstance(model.computed, ComputedField.ObjectProxy)


class TestImproperConfiguration(object):
    def test_null_compute_from(self):
        with pytest.raises(ImproperlyConfigured) as ex:
            class BadModel(models.ComputedText):
                foo = ComputedCharField()
        expected_error = 'ComputedCharField requires setting compute_from'
        assert expected_error == str(ex.value)


class TestValueCoercion(object):
    @pytest.mark.django_db
    def test_date_time_to_date(self):
        computed_date_time_model = models.ComputedDateFromDateTime
        datetime_model_object = computed_date_time_model.objects.create()
        assert isinstance(datetime_model_object.computed, date)
        created_at_date = datetime_model_object.created_at.date()
        assert datetime_model_object.computed == created_at_date
