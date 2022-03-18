from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [ 
        'http://127.0.0.1:8000/auth/users/', # user registration 
        'http://127.0.0.1:8000/auth/jwt/create', # login a user to get access and refresh token 
        'http://127.0.0.1:8000/userapp/userprofile/me/', # request user profile, GET,POST, PUT, request
        'http://127.0.0.1:8000/auth/jwt/refresh', # to get access token from refresh token
        'http://127.0.0.1:8000/userapp/userprofile/', # user profile

    ]
    return Response(routes)
