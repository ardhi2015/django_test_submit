from http.client import responses
from unittest import mock
from urllib import response
from django.test import TestCase
from core.service.views import*



class register_test(TestCase):
  json_fake = [
      {
    "status": "201",
    "message": "string",
    "result": {
    "id": 1,
    "name": "string",
    "email": "string",
    "username": "string"
              }
      }
    ]


  @mock.patch("core.service.serializers.UserSerializer.create", return_value=[])
  def test_register(self, request):
    res = RegisterView.post(self, request)
