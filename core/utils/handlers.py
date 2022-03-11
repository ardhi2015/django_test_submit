from rest_framework.exceptions import NotAuthenticated
from rest_framework.response import Response
from rest_framework.views import exception_handler

from .responses import Responses


def handle_exception(exc, context):
    if isinstance(exc, NotAuthenticated):
        return Response(Responses.error("You should log in first"), status=401)

    return exception_handler(exc, context)
