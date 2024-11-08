from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    turma = models.CharField(max_length=100)
    aprovado = models.BooleanField()
    email = models.EmailField()
    
    