from django.db import models
from django.conf import settings
from django.utils import timezone

class post(models.model):
    autor = models.foreignkey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.charfield(max_length=500)
    texto = models.textfield()
    fecha_creacion = models-datatimefield(default=timezone.now)
    fecha_publicacion = models.datatimefield(black=true, null=true)

    def get_fecha_publicacion(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def _str_(self):
        return self.titulo
        
