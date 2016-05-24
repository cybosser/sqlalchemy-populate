import unittest


class SubstituteExceptionTest(unittest.TestCase):
    def test__expected_exception__substitutes_with_specified(self):
        from sqlalchemy_populate.exceptions import substitute_exception
        from sqlalchemy_populate_tests.stubs import FirstExceptionStub, SecondExceptionStub

        with self.assertRaises(SecondExceptionStub):
            with substitute_exception(FirstExceptionStub, SecondExceptionStub()):
                raise FirstExceptionStub()

    def test__unexpected_exception__does_nothing(self):
        from sqlalchemy_populate.exceptions import substitute_exception
        from sqlalchemy_populate_tests.stubs import FirstExceptionStub, SecondExceptionStub

        with self.assertRaises(SecondExceptionStub):
            with substitute_exception(FirstExceptionStub, SecondExceptionStub()):
                raise SecondExceptionStub()
