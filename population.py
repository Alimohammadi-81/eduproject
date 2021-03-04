import os
import django
from faker import Faker

# set  DJANGO_SETTINGS_MODULE=mysites.settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE','eduproject.settings')
django.setup()

from users.models import RegEmail,UserInfo
fakegen = Faker()

def datagen(N=10):
    for item in range(N):
        fake_f_n = fakegen.first_name()
        fake_l_n = fakegen.last_name()
        fake_mail = fakegen. ascii_free_email()

        rg_ml = RegEmail.objects.get_or_create(Email_addr = fake_mail)[0]
        usr_inf = UserInfo.objects.get_or_create(First_name = fake_f_n, Last_name = fake_l_n,mail = rg_ml)[0]

if __name__ == '__main__':
    print('population Started!')
    datagen(5)
    print('population Finished!')
