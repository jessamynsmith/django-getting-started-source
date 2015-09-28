from django.test import TestCase
from mock import patch
import requests 


from libs.open_weather_map.wrapper import OpenWeatherMap


class OpenWeatherMapTestCase(TestCase):
    def setUp(self):
        # Create a reference to the class being tested
        self.open_weather_map = OpenWeatherMap()

    # Patch out requests.get to avoid making a call to the actual API
    @patch("requests.get")    
    def test_failure(self, mock_get):
        # Set up a response with a failure error code to test error handling
        response = requests.Response()
        response.status_code = requests.codes.bad_request
        # Set the mock to return the failure response
        mock_get.return_value = response

        forecast = self.open_weather_map.get_forecast()

        # Ensure that if an error occurs, we get back an empty object and no exceptions are thrown
        self.assertEqual({}, forecast)

    # Patch out requests.get to avoid making a call to the actual API
    @patch("requests.get")
    def test_success(self, mock_get):
        # Set up a response with a successful error code and some data to test the success case
        response = requests.Response()
        response.status_code = requests.codes.ok 
        response._content = b'{"city": {"name": "Sydney"}}'
        # Set the mock to return the success response
        mock_get.return_value = response

        forecast = self.open_weather_map.get_forecast()

        # Ensure that the data we set in the response body has been parsed correctly
        self.assertEqual("Sydney", forecast['city']['name'])
