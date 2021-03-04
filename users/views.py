from django.shortcuts import render
from users.models import RegEmail,UserInfo
# Create your views here

# no1 = [6,7,8,9,10]
no1 = [0,1,2,3,4]
no2 = [9,10,11,12,13]
def userindex(request):
    usrlst = UserInfo.objects.all()
    mlst = RegEmail.objects.all()
    my_dict={'info':usrlst, 'maillist':mlst}

    return render(request, 'users/userindex.html', context = my_dict)
