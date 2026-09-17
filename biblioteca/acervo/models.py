from django.db import models
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    def __str__(self):
        return self.titulo



    class Livro(models.Model):
        TIPO_CHOICES = [
            ('Físico', 'Físico'),
            ('Digital', 'Digital'),
    ]

    CATEGORIA_CHOICES = [
        ('000', '000 – Generalidades e Informação'),
        ('100', '100 – Filosofia e Psicologia'),
        ('200', '200 – Religião e Teologia'),
        ('300', '300 – Ciências Sociais e Direito'),
        ('400', '400 – Linguística e Idiomas'),
        ('500', '500 – Ciências Puras (Exatas e Naturais)'),
        ('600', '600 – Ciências Aplicadas (Tecnologia)'),
        ('700', '700 – Artes e Recreação'),
        ('800', '800 – Literatura'),
        ('900', '900 – História e Geografia'),
    ]

    titulo = models.CharField(max_length=200, verbose_name="Título")
    autor = models.CharField(max_length=100, verbose_name="Autor")
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='Físico', verbose_name="Tipo de Acervo")
    categoria = models.CharField(max_length=3, choices=CATEGORIA_CHOICES, default='000', verbose_name="Categoria")

    def __str__(self):
        return f"{self.titulo} ({self.tipo})"