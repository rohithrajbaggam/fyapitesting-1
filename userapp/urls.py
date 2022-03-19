from django.urls import path, include
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('userprofile', views.UserProfileViewSet)
router.register('posts', views.UserPostViewSet) # parent router
 # parent router

 
# userposts = routers.NestedDefaultRouter(router, 'userposts', lookup='posts') likes comments all comes under child router
# userposts.register('posts', views.UserPostViewSet, basename='user-posts')


 
urlpatterns = [ 
    path('post-list/', views.post_list_view)
] + router.urls 