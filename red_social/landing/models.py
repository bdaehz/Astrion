from django.db import models
from django.conf import settings

# Create your models here.

class Perfil(models.Model):
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.TextField(max_length=30)
    biografia = models.TextField(max_length=200)

class Publicacion(models.Model):
    id_publicacion = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # id_comentario = models.ForeignKey('Comentario', on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='img/media/')
    fecha = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField(max_length=200)

# class Comentario(models.Model):
#     id_comentario = models.AutoField(primary_key=True)
#     id_publicacion = models.ForeignKey('Publicacion', on_delete=models.CASCADE)
#     id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     contenido = models.TextField(max_length=200)
#     fecha = models.DateTimeField(auto_now_add=True)