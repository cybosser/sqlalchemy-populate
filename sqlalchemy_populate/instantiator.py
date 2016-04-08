import importlib

from sqlalchemy_populate.parsers import parse_model_name


def _get_model_class(model_name):
    module_name, class_name = parse_model_name(model_name)

    module = importlib.import_module(module_name)

    return getattr(module, class_name)


def instantiate_model(model_name, fields):
    model_class = _get_model_class(model_name)

    return model_class(**fields)
