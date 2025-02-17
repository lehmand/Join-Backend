from django.apps import AppConfig
from django.db.models.signals import post_migrate

def load_initial_users(sender, **kwargs):
    """
    Load initial user data from fixtures after migrations.
    """
    from django.core.management import call_command

    # Check if the database already contains users
    from join_auth_app.models import CustomUser
    if CustomUser.objects.exists():
        print("Users already exist. Skipping fixture loading.")
        return

    # Load the users fixture
    try:
        call_command('loaddata', 'users.json')
        print("Successfully loaded users.json")
    except Exception as e:
        print(f"Error loading users.json: {e}")

class JoinAuthAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'join_auth_app'  # Replace with your app name

    def ready(self):
        # Connect the signal handler to the post_migrate signal
        post_migrate.connect(load_initial_users, sender=self)