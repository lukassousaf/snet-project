from django.db import models
from localflavor.br.forms import BRZipCodeField

# Create your models here.


class Client(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    cep = models.CharField(max_length=9)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
