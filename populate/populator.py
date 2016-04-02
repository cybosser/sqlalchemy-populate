import itertools

from populate.instantiator import instantiate_model


def _instantiate(fixture):
    model = instantiate_model(fixture['model'], fixture['fields'])

    model.id = fixture['pk']

    return model


def populate(session, fixtures, commit=True):
    session.add_all(itertools.imap(_instantiate, fixtures))

    if commit:
        session.commit()
