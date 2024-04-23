from django.urls import path , include
from .views import register, login_view, profile
from . import views 
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', profile, name='profile'),
    
    
]