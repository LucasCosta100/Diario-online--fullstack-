from django.apps import AppConfig


class DiarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'diario'



#Para criar esse ambiente usei o código "python manage.py startapp diario", necessario acrescentar no local core/setting a pasta criada no INSTALLED_APPS