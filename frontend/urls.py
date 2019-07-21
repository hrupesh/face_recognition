from django.urls import path ,include
from .views import register
#from rest_framework import routers
#from .api import UserViewSet

urlpatterns = [
    path('', register , name='register'),
]



#router = routers.DefaultRouter()
#router.register('api/users',UserViewSet , 'leads')

#urlpatterns += router.urls 