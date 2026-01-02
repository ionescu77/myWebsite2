from django.apps import AppConfig


class BlogengineConfig(AppConfig):
    """Configuration for the blogengine application.

    Sets the default auto field type to BigAutoField for all models
    in this app, addressing Django 3.2+ warnings about auto-created
    primary keys (models.W042).
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "blogengine"
