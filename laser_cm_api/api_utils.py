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