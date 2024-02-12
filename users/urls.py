
from django.urls import path
from users import views

urlpatterns = [

    path('login/',views.Login__,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('signup/',views.Signup,name='signup'),
    path('forget_password/',views.Forgot_Password,name='forget_password'),
    path('reset_password/',views.Reset_Password,name='reset_password'),
    path('Transections/',views.transections,name='transections'),
    path('personal/',views.personal,name='profile'),
    path('change-password/',views.Reset_Password,name='change_password'),
    
]