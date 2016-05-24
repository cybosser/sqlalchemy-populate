import importlib

from sqlalchemy_populate.exceptions import LoadError, substitute_exception

def load_class(module_name, class_name):
    with substitute_exception(ImportError, LoadError("Couldn't import module '" + module_name + "'")):
        module = importlib.import_module(module_name)

    with substitute_exception(AttributeError, LoadError("Couldn't load class '" + class_name + "' from module '" + module_name + "'")):
        return getattr(module, class_name)
