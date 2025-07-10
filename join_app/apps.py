from django.apps import AppConfig

class JoinAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'join_app'
    verbose_name = 'Join App'

    def ready(self):
        # Ensure join_auth_app is ready first
        from django.apps import apps
        apps.get_app_config('join_auth_app').ready()