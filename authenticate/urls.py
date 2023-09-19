from django.urls import path
from . import views


urlpatterns = [
    path('', views.Registration_page, name='registration'),
    path('login/', views.Login_page, name='login'),
    path('logout/',views.logout_page,name = 'logout'),
    path('home/', views.Home_page, name='home')




]
