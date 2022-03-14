from cgitb import text
from urllib import response
from rest_framework.test import APITestCase
from django.urls import reverse
from jsonpath_rw import jsonpath
from django.shortcuts import render
# from core.service.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
import json



class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.weather_url = reverse('index')

        self.user_data={
            'email':"email1@gmail.com",
            'username':"alien",
            'name':"emailtest1",
            'password': "000"
        }


        self.create_weather_data={
            "date": "2022-03-02",
            "weathercode": 80,
            "max_temperature": 25,
            "min_temperature": 30,
            "sunrise": "2020-03-02 23:42:00",
            "sunset": "2020-03-02 23:42:00",
            "temperature": 25
        }

        self.user_alien={
            'username':"alien",
            'password': "000"
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()


# TestView
    def test_user_get_weather_data(self):
        res = self.client.get(
            self.weather_url)

        self.assertEqual(res.status_code, 200)

    def test_user_create_wather_data(self):
        weather_post = self.client.post(
            self.weather_url, self.create_weather_data, format="json")
        
        #convert json to string
        response_str = json.dumps(weather_post.data)
        # fect value using Json format
        json_response = json.loads(response_str)


        self.assertEqual(weather_post.status_code, 200)


    def test_user_create_wather_data_then_get_it(self):
        weather_post = self.client.post(
            self.weather_url, self.create_weather_data, format="json")
        
        get_weather_data =  self.client.get(
            self.weather_url)
        # import pdb
        # pdb.set_trace()
 
        self.assertEqual(weather_post.status_code, 200)

        self.assertEqual(get_weather_data.status_code, 200)                        



