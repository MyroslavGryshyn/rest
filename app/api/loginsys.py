import hashlib
import json
import random

from django.views.generic import View
from django.http import JsonResponse
from django.contrib import auth

from api.models import Key, CustomUser
from api.utils import error_resp


class Login(View):
    def post(self, request):
        request_as_json = json.loads(request.body.decode('utf-8'))

        email = request_as_json.get('email', None)
        password = request_as_json.get('password', None)

        if email is None or password is None:
            return error_resp(
                422,
                'Unacceptable',
                'Body parameters must be email and password'
            )

        user = auth.authenticate(email=email, password=password)
        if user is None:
            return error_resp(
                401, 'Unauthorized', 'Email or password is invalid')

        api_key = Key.objects.get(user=user)

        return JsonResponse(
            {'message': 'Authorization successful', 'key': api_key.key})


class Logout(View):
    def get(self, request):
        auth.logout(request)
        return JsonResponse({'message': 'Logout successful'})


class Registration(View):
    def post(self, request):
        request_as_json = json.loads(request.body.decode('utf-8'))

        username = request_as_json.get('username', None)
        email = request_as_json.get('email', None)
        password = request_as_json.get('password', None)

        if username is None or email is None or password is None:
            return error_resp(
                422,
                'Unacceptable',
                'Body parameters must be email and password'
            )

        if CustomUser.objects.filter(email=email):
            return error_resp(
                409, 'Conflict', 'User with this email already exists')

        user = CustomUser.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()

        api_key = self._get_api_key()
        key = Key(user=user, key=api_key)
        key.save()

        return JsonResponse(
            {'message': 'Registration successful', 'key': api_key})

    @staticmethod
    def _get_api_key():
        key = hashlib.md5(str(random.random()).encode())
        return key.hexdigest()
