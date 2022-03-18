from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from django.shortcuts import render
from .models import UserProfile, Post
from .serializers import UserProfileSerializer, UserPostSerializer
from .permissions import IsAuthorOrReadOnly, IsUserProfileorReadOnly

# Create your views here.
class UserProfileViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsUserProfileorReadOnly]


    @action(detail=False, methods=['GET', 'PUT']) # we can add permission classes as another argument  # if detail is True models.object.get type detailview ? False models.object.all listview
    def me(self, request):
        (userprofile, created) = UserProfile.objects.get_or_create(user=request.user)
        if request.method == 'GET':
            serializer = UserProfileSerializer(userprofile)
            return Response(serializer.data)
        elif request.method == 'PUT' and request.user == userprofile.user:
            serializer = UserProfileSerializer(UserProfile, data=request.data)
            # userprofile.user = request.user
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)



@api_view(['GET'])
def post_list_view(request):
    queryset = Post.objects.all()
    serializers = UserPostSerializer(queryset, many=True)
    return Response(serializers.data)




# class UserPostViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
#     queryset = Post.objects.all()
#     serializer_class = UserPostSerializer

class UserPostViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = UserPostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    
    @action(detail=False, methods=['GET', 'PUT'])
    def me(self, request):
        queryset = Post.objects.all()
        if request.method == 'GET':
            serializer = UserPostSerializer(queryset)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = UserPostSerializer(Post, data=request.sata)

            return Response(serializer.data)
        elif request.user == queryset.author :
            if request.method == 'PUT':
                serializer = UserPostSerializer(Post, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data)




