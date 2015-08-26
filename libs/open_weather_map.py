import requests


class OpenWeatherMap(object):

    def __init__(self):
        self.api_url = 'http://api.openweathermap.org/data/2.5/'

    def get_forecast(self):
        # Append the "forecast" path to the base API URL
        url = '%sforecast' % self.api_url

        # URL parameters
        params = {
            'lat': -33.8650,
            'lon': 151.2094
        }

        # Do a get request on the forecast url, with the lat/lon params
        response = requests.get(url, params=params)

        # It's always a good idea to initialize results to empty, and update if data received
        results = {}
        # If the request was successful
        if response.status_code == requests.codes.ok:
            # Get the response body in JSON format
            results = response.json()

        return results
