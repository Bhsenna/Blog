from django.db import models
from django.utils import timezone

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Autor(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Pagina(models.Model):
    data = models.DateTimeField(default=timezone.now)
    conteudo = models.TextField()
    categorias = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    descricao = models.TextField(blank=True)
    titulo = models.CharField(max_length=40)
    imagem = models.CharField(max_length=500, blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.titulo
