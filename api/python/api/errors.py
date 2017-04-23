class APIException(Exception):
    pass


class NoSuchResource(APIException):
    message = 'resource not found'
    status = 404


error_index = {
    klass.__name__: dict(message=klass.message, status=klass.status)
    for klass in [
        NoSuchResource,
    ]
}
