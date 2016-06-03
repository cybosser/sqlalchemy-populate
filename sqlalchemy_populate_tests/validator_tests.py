import unittest

from nose_parameterized import parameterized


class ValidateFixturesTest(unittest.TestCase):
    def test__missing_model_name__throws_exception(self):
        from sqlalchemy_populate.validator import validate_fixture
        from sqlalchemy_populate.validator import ValidationError

        fixture = {
            'pk': 1,
            'fields': {
                'name': 'value'
            }
        }

        with self.assertRaises(ValidationError):
            validate_fixture(fixture)

    @parameterized.expand([
        ({'model': 'package.module.class'},),
        ({'model': 'package.module.class', 'pk': 1},),
        ({'model': 'package.module.class', 'pk': 1, 'fields': {}},),
        ({'model': 'package.module.class', 'pk': 1, 'fields': {'name': 'value'}},)
    ])
    def test__valid_fixture__does_nothing(self, fixture):
        from sqlalchemy_populate.validator import validate_fixture

        validate_fixture(fixture)

    def test__unknown_field__throws_exception(self):
        from sqlalchemy_populate.validator import validate_fixture, ValidationError

        fixture = {
            'model': 'package.module.model',
            'pk': 1,
            'fields': {
                'name': 'value'
            },
            '__unknown__': 42
        }

        with self.assertRaises(ValidationError):
            validate_fixture(fixture)
