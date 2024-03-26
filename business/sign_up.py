# import json
import base64
import random
import string
from django.http import HttpResponse

from .models import Users
from .models import Languagetable

from third_party_api_services import ThirdPartyApi
from sns_activities import SnsActivities


class SignUp(object):

    @staticmethod
    def password_encryption(password):

        encrypted_password = base64.b64encode("password".encode("utf-8"))

        return encrypted_password

    @staticmethod
    def create_user_token():

        while True:

            user_token = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
            available_token = list(Users.objects.filter(usertoken=user_token).values('usertoken'))

            if len(available_token) == 0:
                break

        return user_token

    @staticmethod
    def sign_up(request):

        if request.method == "POST":

            user_name = request.POST.get('UserName')

            # Creating the User Token
            user_token = SignUp.create_user_token()

            email_id = request.POST.get('EmailID')

            # Password Encryption
            password = request.POST.get('Password')
            encrypted_password = SignUp.password_encryption(password)

            dob = request.POST.get("DOB")
            birth_location = request.POST.get('POB')

            birth_lat_long_details = ThirdPartyApi.google_lat_long_api(birth_location)
            birth_latitude = birth_lat_long_details['Latitude']
            birth_longitude = birth_lat_long_details['Longitude']
            birth_offset = request.POST.get('BirthOffset')

            primary_location = request.POST.get('PrimaryLocation')
            primary_lat_long_details = ThirdPartyApi.google_lat_long_api(primary_location)
            primary_latitude = primary_lat_long_details['Latitude']
            primary_longitude = primary_lat_long_details['Longitude']
            primary_offset = request.POST.get('PrimaryOffset')

            user_type = "NOOB"
            language = request.POST.get('Language')

            data = Users(username=user_name, usertoken=user_token, email=email_id,
                         password=encrypted_password, dateofbirth=dob, birthlocation=birth_location,
                         birthlatitude=birth_latitude, birthlongitude=birth_longitude, birth_offset=birth_offset,
                         primarylocation=primary_location, primarylatitude=primary_latitude,
                         primarylongitude=primary_longitude, primary_offset=primary_offset, usertype=user_type)
            data.save()

            # Amazon SNS
            firebase_token = request.POST.get('FirebaseToken')
            created_arn = SnsActivities.create_new_user(user_token, email_id, firebase_token)

            # Sending Welcome Notification
            lang_id = f"message{language}".lower()
            message = Languagetable.objects.filter(messageid=1).values(f'{lang_id}')[0][lang_id]
            SnsActivities.welcome_notification(created_arn, message)

            json_response = {'SuccessFlag': 'Y',
                             'Details': [{'Caption': 'Title',
                                          'Text': "You've Successfully signed in.",
                                          'Link': "app:dashboard link"}]}

            return HttpResponse(json_response, content_type='application/json')
