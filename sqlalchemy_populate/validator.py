import jsonschema

from sqlalchemy_populate.exceptions import ValidationError
from sqlalchemy_populate.schemas import FIXTURE_SCHEMA


def validate_fixture(fixture):
    try:
        jsonschema.validate(fixture, FIXTURE_SCHEMA)
    except jsonschema.ValidationError as e:
        raise ValidationError(str(e))
