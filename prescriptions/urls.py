from django.urls import path
from . import views
urlpatterns=[
    path('addpres/',views.addpres,name='addpres'),
    path('showpres/',views.showpres,name='showpres'),
    path('showmedhis/',views.showmedhis,name='showmedhis'),
]