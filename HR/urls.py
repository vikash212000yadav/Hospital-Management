from django.urls import path
from . import views

urlpatterns=[
    path('dashboard/',views.dashboard,name='dashboard'),
    path('deletedoc/',views.deletedoc,name='deletedoc'),
    path('createdoc/',views.createdoc,name='crtdoc'),
    path('updatedoc/',views.updatedoc,name='updatedoc'),
    path('accounting/',views.accounting,name='accounting'),
    path('showinvoice/',views.show,name='show'),
    path('send/',views.send,name='send'),
    path('payments/',views.payments,name='payments'),
]