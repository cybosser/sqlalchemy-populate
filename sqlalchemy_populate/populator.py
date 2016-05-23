import itertools

from sqlalchemy_populate.loader import load_class
from sqlalchemy_populate.parsers import parse_model_name
from sqlalchemy_populate.validator import validate_fixtures


def _instantiate(fixture):
    module_name, class_name = parse_model_name(fixture['model'])

    model = load_class(module_name, class_name)(**fixture['fields'])

    primary_key = fixture.get('pk')
    if primary_key:
        model.id = primary_key

    return model


def populate(session, fixtures):
    validate_fixtures(fixtures)

    session.add_all(itertools.imap(_instantiate, fixtures))
