from django.db import models
from django.utils import timezone

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Pagina(models.Model):
    data = models.DateTimeField(default=timezone.now)
    conteude = models.TextField()
    categorias = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    descricao = models.TextField(blank=True)
    titulo = models.CharField(max_length=20)
    imagem = models.CharField(max_length=15)
    autor = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
