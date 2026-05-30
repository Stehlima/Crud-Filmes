from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome da Categoria")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['nome']

class Filme(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    diretor = models.CharField(max_length=200, verbose_name="Diretor")
    ano_lancamento = models.IntegerField(verbose_name="Ano de Lançamento")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="filmes", verbose_name="Categoria")
    capa = models.ImageField(upload_to='capas/', blank=True, null=True, verbose_name="Capa do Filme")
    capa_url = models.URLField(blank=True, null=True, verbose_name="URL da Capa")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"
        ordering = ['titulo']
