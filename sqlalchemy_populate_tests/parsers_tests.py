import unittest

from nose_parameterized import parameterized


class ParseModelNameTests(unittest.TestCase):
    @parameterized.expand([
        ('module.class', ('module', 'class')),
        ('package.module.class', ('package.module', 'class')),
    ])
    def test__valid_model_name__returns_module_and_class_names(self, model_name, expected):
        from sqlalchemy_populate.parsers import parse_model_name

        actual = parse_model_name(model_name)

        self.assertEqual(expected, actual)

    @parameterized.expand([
        'class',
        'module/package',
    ])
    def test__invalid_model_name__throws_exception(self, model_name):
        from sqlalchemy_populate.exceptions import FormatError
        from sqlalchemy_populate.parsers import parse_model_name

        with self.assertRaises(FormatError):
            parse_model_name(model_name)
