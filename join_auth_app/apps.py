from django.apps import AppConfig
from django.db.models.signals import post_migrate

def load_initial_users(sender, **kwargs):
    """
    Load initial user data from fixtures after migrations.
    """
    from django.core.management import call_command

    from join_auth_app.models import CustomUser
    if CustomUser.objects.exists():
        print("Users already exist. Skipping fixture loading.")
        return

    try:
        call_command('loaddata', 'initial_users.json')
        print("Successfully loaded users.json")
    except Exception as e:
        print(f"Error loading users.json: {e}")

class JoinAuthAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'join_auth_app'  # Replace with your app name
    verbose_name = 'Join Auth App'

    def ready(self):
        post_migrate.connect(load_initial_users, sender=self)