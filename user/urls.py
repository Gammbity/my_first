from django.urls import path
from .views import registration_view,Login_view,Logout_view,profile_view

urlpatterns = [
    path ('profile/', profile_view, name='profile'),
    path ('logout/', Logout_view, name='logout'),
    path ('registrations/', registration_view, name='registration'),
    path ('login/', Login_view, name='login'),  
]
