import re

from sqlalchemy_populate.exceptions import FormatError


def parse_model_name(model_name):
    match = re.search('^((?:\w+\.?)+)\.(\w+)$', model_name)
    if not match:
        raise FormatError(u'Invalid model name: ' + model_name)

    return match.groups()
