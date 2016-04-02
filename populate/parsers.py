import re


def parse_model_name(model_name):
    match = re.search('^((?:\w+\.?)+)\.(\w+)$', model_name)
    if not match:
        raise RuntimeError(u'Invalid model name: ' + model_name)

    return match.groups()
