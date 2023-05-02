from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Aboutus', views.Aboutus, name='Aboutus'),
    path("home", views.home, name='home'),
    path("contactus", views.contactus, name='contactus'),
    path('login', views.login, name='login'),
    path('loginfailed', views.loginfailed, name="loginfailed"),
    path('Output', views.User1, name="Output"),
    path('Register1', views.Register1, name="Register1"),
    path('Register', views.Register, name="Register"),
    path('my_redirect1', views.my_redirect1, name="my_redirect1"),
    path('rhome2', views.rhome2, name="rhome2"),
    
]











