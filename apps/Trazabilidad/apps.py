from django.apps import AppConfig

class TrazabilidadConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.Trazabilidad"

    def ready(self):
        print("Cargando señales de Trazabilidad...")
        import apps.Trazabilidad.socket.signals  # Importar las señales
        print("Señales cargadas.")
