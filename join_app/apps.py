from django.apps import AppConfig
from django.db.models.signals import post_migrate

class JoinAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'join_app'  # Replace with your app name
    verbose_name = 'Join App'

    # Specify that join_app depends on join_auth_app
    def ready(self):
        # Ensure join_auth_app is ready first
        from django.apps import apps
        apps.get_app_config('join_auth_app').ready()

        # Connect the signal handler to the post_migrate signal
        post_migrate.connect(load_initial_data, sender=self)

def load_initial_data(sender, **kwargs):
    """
    Load initial data from fixtures after migrations.
    """
    from django.core.management import call_command

    # Check if the database already contains data
    from join_app.models import Task  # Replace with any model to check for existing data
    if Task.objects.exists():
        print("Database already contains data. Skipping fixture loading.")
        return

    # List of fixture files to load (in the correct order)
    fixtures = [
        'initial_contacts.json',  # Fixture for Contact (depends on CustomUser)
        'initial_tasks.json',  # Fixture for Task (depends on Contact)
        'initial_subtasks.json',  # Fixture for SubTask (depends on Task)
    ]

    # Load each fixture
    for fixture in fixtures:
        try:
            call_command('loaddata', fixture)
            print(f"Successfully loaded {fixture}")
        except Exception as e:
            print(f"Error loading {fixture}: {e}")