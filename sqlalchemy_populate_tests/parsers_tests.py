import unittest

from nose_parameterized import parameterized


class ParseModelNameTests(unittest.TestCase):
    @parameterized.expand([
        ('module.class', 'module', 'class'),
        ('package.module.class', 'package.module', 'class'),
    ])
    def test_valid_model_name_returns_module_and_class_names(self, model_name, expected_module_name, expected_class_name):
        from sqlalchemy_populate.parsers import parse_model_name

        module_name, class_name = parse_model_name(model_name)

        self.assertEqual(expected_module_name, module_name)
        self.assertEqual(expected_class_name, class_name)

    @parameterized.expand([
        'class',
        'module/package',
    ])
    def test_invalid_model_name_throws_format_error(self, model_name):
        from sqlalchemy_populate.exceptions import FormatError
        from sqlalchemy_populate.parsers import parse_model_name

        with self.assertRaises(FormatError):
            parse_model_name(model_name)
