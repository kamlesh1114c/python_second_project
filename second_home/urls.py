from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('forgot/',views.forgot,name='forgot'),
    path('verify_otp',views.verify_otp,name='verify_otp'),
    
]
