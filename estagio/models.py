from django.db import models
import os
import uuid
from django.contrib.auth.models import User
# Create your models here.
def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return os.path.join("files", filename)

class Estagio(models.Model):
    file = models.FileField(upload_to=user_directory_path, null=True)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    postar = models.BooleanField(default=False)
    class Meta:
         permissions = (("est", "est"),("ed", "ed"), ("exc", "exc"),)