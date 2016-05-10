import unittest


class ParseModelNameTests(unittest.TestCase):
    def test_valid_model_name_returns_module_and_class_names(self):
        from sqlalchemy_populate.parsers import parse_model_name

        MODEL_NAMES = (
            ('module.model', 'module', 'model'),
            ('package.module.model', 'package.module', 'model')
        )

        for model_name, module_name_expected, class_name_expected in MODEL_NAMES:
            module_name, class_name = parse_model_name(model_name)

            self.assertEqual(module_name, module_name_expected)
            self.assertEqual(class_name, class_name_expected)

    def test_invalid_model_name_throws_format_error(self):
        from sqlalchemy_populate.exceptions import FormatError
        from sqlalchemy_populate.parsers import parse_model_name

        MODEL_NAMES = ('model', 'module/package')

        for model_name in MODEL_NAMES:
            with self.assertRaises(FormatError):
                parse_model_name(model_name)
