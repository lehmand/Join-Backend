from django.urls import include, path
from .views import RegistrationList, UserList, UserDetail, CustomAuthToken
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('registration/', RegistrationList.as_view(), name='registration'),
    path('login/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>', UserDetail.as_view(), name='user-detail'),
]
