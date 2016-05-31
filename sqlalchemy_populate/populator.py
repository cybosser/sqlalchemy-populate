import itertools

from sqlalchemy_populate.loader import load_class
from sqlalchemy_populate.parsers import parse_model_name
from sqlalchemy_populate.validator import validate_fixture


def _validate_fixtures(fixtures):
    for fixture in fixtures:
        validate_fixture(fixture)


def _instantiate_fixture(fixture):
    module_name, class_name = parse_model_name(fixture['model'])

    model = load_class(module_name, class_name)(**fixture['fields'])

    primary_key = fixture.get('pk')
    if primary_key:
        model.id = primary_key

    return model


def populate(session, fixtures):
    _validate_fixtures(fixtures)

    session.add_all(itertools.imap(_instantiate_fixture, fixtures))
