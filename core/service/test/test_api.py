from rest_framework.test import APITestCase
from django.urls import reverse
from jsonpath_rw import jsonpath
from django.shortcuts import render
from core.service.models import User



class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')

        self.user_data={
            'email':"email1@gmail.com",
            'username':"alien",
            'name':"emailtest1",
            'password': "000"
        }

        self.user_alien={
            'username':"alien",
            'password': "000"
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()


# TestView
class TestViews(TestSetUp):
    def test_user_cannot_register_with_no_data(self):
        res=self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_user_can_register_correctly(self):
        res=self.client.post(
            self.register_url, self.user_data, format="json")

        # self.assertEqual(res.data['result'][0]['email'] == self.user_data['email'])
        # self.assertEqual(res.data['username'], self.user_data['username'])
        self.assertEqual(res.status_code, 201)

    def test_user_cannot_login_with_unregistered_user(self):
        res=self.client.post(
            self.login_url, self.user_data, format="json")
        self.assertEqual(res.status_code, 400)

    def test_user_login_with_registered_user(self):
        self.client.post(
            self.register_url, self.user_data, format="json")

        login=self.client.post(
            self.login_url, self.user_alien, format="json")
        # self.assertEqual(res.data, {'status': 'success', 'message': 'Login successful'})
        self.assertEqual(login.status_code, 200)



