import importlib
import itertools
import re


def _parse_model_name(model_name):
    match = re.search('^((?:\w+\.?)+)\.(\w+)$', model_name)
    if not match:
        raise RuntimeError(u'Invalid model name: ' + model_name)
    return match.groups()


def _get_model_class(model_name):
    module_name, class_name = _parse_model_name(model_name)

    module = importlib.import_module(module_name)

    return getattr(module, class_name)


def _instantiate_impl(model_name, pk, fields):
    model_class = _get_model_class(model_name)

    model = model_class(**fields)
    model.id = pk

    return model


def _instantiate(fixture):
    return _instantiate_impl(fixture['model'], fixture['pk'], fixture['fields'])


def populate(session, fixtures, commit=True):
    session.add_all(itertools.imap(_instantiate, fixtures))

    if commit:
        session.commit()
