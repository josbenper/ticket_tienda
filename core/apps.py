from django.apps import AppConfig

class PresionConfig(AppConfig):
    name = 'core'
    verbose_name = 'Core'
 
    def ready(self):
        import core.signals

