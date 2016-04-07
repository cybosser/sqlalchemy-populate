import itertools

from populate.instantiator import instantiate_model
from populate.validator import validate_fixtures


def _instantiate(fixture):
    model = instantiate_model(fixture['model'], fixture['fields'])

    model.id = fixture['pk']

    return model


def populate(session, fixtures):
    validate_fixtures(fixtures)

    session.add_all(itertools.imap(_instantiate, fixtures))
