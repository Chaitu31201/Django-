import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Level2.settings')
import django
from random import seed,randint
django.setup()
from App1.models import User,Guest
from faker import Faker
print('Working..')
fakegen = Faker()
def populate(n = 5):
    for i in range(5):
        fake_uname = fakegen.name()
        fake_age = randint(20,100)
        fake_phno = fakegen.phone_number()
        fake_vehno = fakegen.name()
        usr = User.objects.get_or_create(uname = fake_uname,age = fake_age,phno = fake_phno)[0]
        gust = Guest.objects.get_or_create(name = fake_uname,age = fake_age,vehicle_no = fake_vehno)[0]
if __name__ == '__main__':
    print('started populating....')
    populate()
    print("Successfully populated.")
