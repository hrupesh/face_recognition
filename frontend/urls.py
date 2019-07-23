from django.urls import path ,include
from .views import register,upload
from rest_framework import routers
from .api import UserViewSet

urlpatterns = [
    path('', register , name='register'),
    path('upload', upload , name='upload'),
]



router = routers.DefaultRouter()
router.register('api/users',UserViewSet , 'leads')

urlpatterns += router.urls 