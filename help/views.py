from django.shortcuts import render

# Create your views here.
def helpfile(request):
    dict1 = {'helppage':'Please contact us via info@hamejaclass.com'}
    return render(request,'help/helpfile.html',context=dict1)
