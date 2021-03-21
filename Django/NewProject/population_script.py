import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','NewProject.settings')
import django
from random import seed,randint
django.setup()
from newApp.models import User
from faker import Faker
print('Working..')
fakegen = Faker()
def populate(n = 5):
    for i in range(5):
        fake_fname = fakegen.name()
        fake_lname = fakegen.name()
        fake_email = fakegen.email()
        usr = User.objects.get_or_create(first_name = fake_fname,last_name = fake_lname,email = fake_email)[0]
if __name__ == '__main__':
    print('started populating....')
    populate()
    print("Successfully populated.")
