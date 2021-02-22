from django.conf.urls import url
from django.urls import path
from help import views

urlpatterns = [
    path('',views.helpfile, name= 'helpfile')
]
