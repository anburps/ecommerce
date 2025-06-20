from django.urls import path
from . import views
from account import views as account

urlpatterns = [
    path('login/', account.login, name='login'),
    path('register/', account.register, name='register'),
    path('logout/', account.logout, name='logout'),
    path('', views.product_list, name='product_list'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),

]
