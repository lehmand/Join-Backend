#!/usr/bin/env python
import os
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'join_backend.settings')
django.setup()

from join_auth_app.models import CustomUser

# Create guest user
guest_user, created = CustomUser.objects.get_or_create(
    email='guest@test.com',
    defaults={
        'username': 'guest',
        'first_name': 'Guest',
        'last_name': 'User'
    }
)

if created:
    guest_user.set_password('asdfasdf')
    guest_user.save()
    print(f"Created guest user: {guest_user.email}")
else:
    print(f"Guest user already exists: {guest_user.email}")

print(f"User ID: {guest_user.id}")