import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_portfolio.settings')
django.setup()
from django.contrib.auth.models import User
u = User.objects.get(username='yonathan')
u.set_password('facil123')
u.save()
print('Password set to facil123')