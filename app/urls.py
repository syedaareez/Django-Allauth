from django.urls import path
from .views import Home,register,login,signup,signin,logout

app_name='basic_app'

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('accounts/profile/',Home.as_view(),name='home2'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('logout/',logout,name='logout'),
]