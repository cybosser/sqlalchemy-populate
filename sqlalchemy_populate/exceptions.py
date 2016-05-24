import contextlib


class ValidationError(Exception):
    pass


class FormatError(Exception):
    pass


@contextlib.contextmanager
def substitute_exception(expected_exception_class, exception_object):
    try:
        yield
    except expected_exception_class:
        raise exception_object
