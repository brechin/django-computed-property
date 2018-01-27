from datetime import date, datetime

import pytest
from django.core.exceptions import ImproperlyConfigured

from computed_property import ComputedCharField, ComputedField
from . import models


@pytest.mark.parametrize(
    'model,vals',
    [
        (models.ComputedText,
         ['baz', 'char has baz', 'test']),
        (models.ComputedChar,
         ['one', 'char has one', 'test']),
        (models.ComputedEmail,
         ['a@example.com', 'testa@example.com', 'garbage@example.com']),
        (models.ComputedInt,
         [1, 1001, 9999]),
        (models.ComputedDate,
         [date(2015, 2, 5), date(2015, 2, 5), date(2019, 4, 1)]),
        (models.ComputedDateTime,
         [datetime(2015, 2, 5, 15),
          datetime(2015, 2, 6, 15),
          datetime(2015, 4, 1, 15)],),
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
        created = model.objects.create(base_value=vals[2])
        assert vals[1] != created.computed
        created.base_value = vals[0]
        created.save()
        assert vals[1] == created.computed

    def test_live_modification(self, db, model, vals):
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
