import itertools

from sqlalchemy_populate.instantiator import instantiate_model
from sqlalchemy_populate.validator import validate_fixtures


def _instantiate(fixture):
    model = instantiate_model(fixture['model'], fixture['fields'])

    pk = fixture.get('pk', None)
    if pk is not None:
        model.id = pk

    return model


def populate(session, fixtures):
    validate_fixtures(fixtures)

    session.add_all(itertools.imap(_instantiate, fixtures))