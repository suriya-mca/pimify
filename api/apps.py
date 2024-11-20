from django.apps import AppConfig

class ApiConfig(AppConfig):
    """
    Configuration class for the API application.
    This class manages the application's configuration and initialization.
    """
    
    # Specify the default primary key type for models
    default_auto_field = "django.db.models.BigAutoField"
    
    # The name of the application
    name = "api"
    
    def ready(self):
        """
        Method called when the application is ready.
        Import models here to ensure all signals and model registration happen properly.
        This is particularly useful for loading signal handlers defined in models.py
        """
        import api.models
