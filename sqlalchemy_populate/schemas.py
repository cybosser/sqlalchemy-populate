FIXTURES_SCHEMA = {
    'type': 'array',
    'items': {
        'type': 'object',
        'properties': {
            'model': {'type': 'string'},
            # TODO: add non-integer primary keys support
            'pk': {'type': 'integer'},
            'fields': {'type': 'object'}
        },
        'required': ['model']
    }
}