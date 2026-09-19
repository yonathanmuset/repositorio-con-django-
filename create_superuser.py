import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_portfolio.settings')
import django
django.setup()
from django.core.management import call_command
call_command('createsuperuser', username='yonathan', password='password123', email='yonathan@example.com', verbosity=2)