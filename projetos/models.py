from django.db import models



# Create your models here.

class Projeto(models.Model):

    titulo = models.CharField(max_length=30)
    descricao = models.TextField(max_length=250, blank=True, null=True)
    link = models.URLField(max_length=60, null=True)
    video = models.FileField(upload_to='videos')
    

    def __str__(self):
        return self.titulo


class Emails(models.Model):
    assunto = models.CharField(max_length=100)
    corpo = models.TextField()
    enviado = models.BooleanField()

    def __str__(self):
        return self.assunto
