import os
import requests
from dotenv import load_dotenv

load_dotenv()


class ThirdPartyApi(object):

    @staticmethod
    def google_lat_long_api(place_of_birth):

        key = os.getenv('GOOGLE_LOCATION_API_KEY')

        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={place_of_birth}&key={key}"
        response = requests.get(url)
        resp_json_payload = response.json()
        latitude = resp_json_payload['results'][0]['geometry']['location']['latitude']
        longitude = resp_json_payload['results'][0]['geometry']['location']['longitude']

        return {'Latitude': latitude, 'Longitude': longitude}
