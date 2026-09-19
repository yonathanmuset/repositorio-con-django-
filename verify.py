from django.core.management import call_command
call_command('createsuperuser', username='yonathan', password='password123', email='yonathan@example.com', verbosity=2)