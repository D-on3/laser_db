from rest_framework.authtoken.models import Token
from accounts.models import Activation  # Import your UserProfile model
import requests
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "laser_db.settings")
import django
django.setup()
from rest_framework.authtoken.models import Token
from accounts.models import Activation  # Import your UserProfile model
import requests

def api_request_with_user_token(user):
    """
    The function `api_request_with_user_token` makes an API request using a user's
    token and returns the response data if the request is successful.

    :param user: The "user" parameter is the user object that represents the user
    making the API request. It is used to retrieve the user's token from the
    Activation model
    :return: The function `api_request_with_user_token` returns the API response
    data if the API request is successful (status code 200). If there is an error
    or the user does not have a token, it returns `None`.
    """
    try:
        user_profile = Activation.objects.get(user=user)
        user_token = user_profile.token

        # Make API requests using user_token
        headers = {
            'Authorization': f'Token {user_token}'
        }

        api_url = 'https://your-api-url.com/endpoint/'
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data  # Return the API response data
        else:
            return None  # Handle API error response

    except Activation.DoesNotExist:
        return None  # Handle the case where the user profile or token does not exist