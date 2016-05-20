import importlib

from sqlalchemy_populate.parsers import parse_model_name


def load_model_class(model_name, model_name_parser=parse_model_name):
    module_name, class_name = model_name_parser(model_name)

    module = importlib.import_module(module_name)

    return getattr(module, class_name)
