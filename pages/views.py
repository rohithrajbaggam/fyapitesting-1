from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from .serializers import PageSerializer
from .models import Page
from .permissions import IsPageAdminOrReadOnly


# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [ 
        'http://127.0.0.1:8000/auth/users/', # user registration 
        'http://127.0.0.1:8000/auth/jwt/create', # login a user to get access and refresh token 
        'http://127.0.0.1:8000/auth/jwt/refresh', # to get access token from refresh token
        
        'http://127.0.0.1:8000/api/userapp/userprofile/me/', # request user profile, GET,POST, PUT, request
        'http://127.0.0.1:8000/api/userapp/userprofile/', # user profile

        'http://127.0.0.1:8000/api/userapp/posts/', # post create page
        'http://127.0.0.1:8000/api/userapp/posts/<int:pk>/', # post detail page put and delete options are allowed for post authors only 
        'http://127.0.0.1:8000/api/userapp/post-list/', # user post list
    
        'http://127.0.0.1:8000/api/pageprofile/', # creating a page
        'http://127.0.0.1:8000/api/pageprofile/<uuid:id>/', # page detail page put and delelte request's are allowed for only admin of the page
        'http://127.0.0.1:8000/api/page-list/', # Page List


    ]
    return Response(routes) 


class PageViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [IsPageAdminOrReadOnly, IsAuthenticated]


class PageViewList(ListModelMixin, GenericViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
