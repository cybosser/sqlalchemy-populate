import unittest


class LoadClassTests(unittest.TestCase):
    def test__invalid_module_name__throws_exception(self):
        from sqlalchemy_populate.loader import load_class

        with self.assertRaises(ImportError):
            class_ = load_class('__invalid_module__', 'ModelStub')

    def test__invalid_class_name__throws_exception(self):
        from sqlalchemy_populate.loader import load_class

        with self.assertRaises(AttributeError):
            class_ = load_class('sqlalchemy_populate_tests.stubs', '__invalid_class__')

    def test__valid_module_and_class_names__returns_class_object(self):
        from sqlalchemy_populate.loader import load_class
        from sqlalchemy_populate_tests.stubs import ModelStub

        class_ = load_class('sqlalchemy_populate_tests.stubs', 'ModelStub')

        self.assertTrue(class_ is ModelStub)
