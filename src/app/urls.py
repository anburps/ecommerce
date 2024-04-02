
from django.urls import path
from .import views


urlpatterns = [
    path('',views.api_product,name='index'),


]