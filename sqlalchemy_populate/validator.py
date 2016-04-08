import jsonschema

from sqlalchemy_populate.exceptions import ValidationError
from sqlalchemy_populate.schemas import FIXTURES_SCHEMA


def validate_fixtures(fixtures):
    try:
        jsonschema.validate(fixtures, FIXTURES_SCHEMA)
    except jsonschema.ValidationError as e:
        raise ValidationError(str(e))
