from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def course(request):
    return HttpResponse('<h1>My New Page About Courses!</h1>')
