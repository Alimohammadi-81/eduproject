from django.conf.urls import url
from django.urls import path
from coursedescript import views

urlpatterns = [
    path('',views.course,name='course'),
]
