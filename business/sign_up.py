import json
import random
import string
from django.http import HttpResponse
from .models import Users


class SignUp(object):

    @staticmethod
    def create_user_token():

        user_token = ''

        for i in range(10):

            user_token = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
            available_token = list(Users.objects.filter(usertoken='GKR2Y9').values('usertoken'))

            if len(available_token) == 0:
                break

        return user_token

    @staticmethod
    def sign_up(request):

        if request.method == "POST":

            name = request.POST.get('UserName')
            dob = request.POST.get("DOB")
            pob = request.POST.get('Location')


            user_token =

            result = {'SuccessFlag': 'Y',
                      'MasterName': name,
                      'Details': [{'Name': 'Aravindh',
                                   'RollNumber': '5'},
                                  {'Name': 'Ajay',
                                   'RollNumber': '8'}]}

        return HttpResponse(json_response, content_type='application/json')
