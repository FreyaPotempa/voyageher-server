from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from voyageherapi.models import Traveler, Guide


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    '''Handles the authentication of a traveler

    Method arguments:
      request -- The full HTTP request object
    '''
    username = request.data['username']
    password = request.data['password']

    is_guide = 'is_guide' in request.data and request.data["is_guide"]

    if is_guide:
        user = authenticate(username=username,
                            password=password, is_guide=True)
    else:
        user = authenticate(username=username, password=password)

    # If authentication was successful, respond with their token
    if user is not None:
        token = Token.objects.get(user=user)
        data = {
            'valid': True,
            'token': token.key
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = {'valid': False}
        return Response(data)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    '''Handles the creation of a new traveler for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    is_guide = 'is_guide' in request.data and request.data['is_guide']
    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    new_user = User.objects.create_user(
        username=request.data['username'],
        password=request.data['password'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name']
    )

    if is_guide:
        guide = Guide.objects.create(
            location_id=request.data['location_id'], bio=request.data['bio'], user=new_user)
        user_type = 'guide'
        user_obj = guide
    else:
        traveler = Traveler.objects.create(
            bio=request.data['bio'],
            user=new_user
        )
        user_type = 'traveler'
        user_obj = traveler

    # Use the REST Framework's token generator on the new user account
    token = Token.objects.create(user=user_obj.user)
    # Return the token to the client
    data = {'token': token.key,
            'user_type': user_type}
    return Response(data)
