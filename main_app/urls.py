from django.urls import path
from . import views

urlpatterns = [
    #home route
    path('', views.home, name='home'),

    path('accounts/signup', views.signup, name='signup'),
    
    path('profile/', views.profile, name='profile'),

    path('about/', views.about, name='about'),
]

