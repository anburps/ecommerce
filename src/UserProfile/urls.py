from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns = [
     path('signup', views.signup, name = 'signup'),
     path('signin', views.signin, name = 'signin'),
     path('signout', views.signout, name = 'signout'),
     # path('changeaddress', views.changeAddress, name = 'changeaddress'),
]
 