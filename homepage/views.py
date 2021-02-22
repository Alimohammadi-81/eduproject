from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(request):
#     return HttpResponse('<em>Hello,I am Ali Mohammadi</em>')

def sample(request1):
    my_dict = {'insert_me':'this is from views.py in home page app!'}
    return render(request1,'homepage/sample.html',context=my_dict)
