from django.urls import path
from . import views
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('pageprofile', views.PageViewSet)


urlpatterns = [ 
    path('', views.getRoutes, name='home'),
    path('page-list/', views.PageViewList.as_view({'get': 'list'}), name='page-list')
] + router.urls
