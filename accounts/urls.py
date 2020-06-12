from django.urls import path
from . import views

urlpatterns=[
    path('register/',views.register,name="register"),
    path('login/',views.login,name='login'),
    path('verify/',views.verify,name='verify'),
    path('uprofile',views.uprofile,name='uprofile'),
    path('profile',views.profile,name='profile'),
    path('logout/',views.logout,name='logout'),
]