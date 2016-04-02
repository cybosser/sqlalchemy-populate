import jsonschema

from populate.schemas import FIXTURES_SCHEMA


def validate_fixtures(fixtures):
    jsonschema.validate(fixtures, FIXTURES_SCHEMA)
