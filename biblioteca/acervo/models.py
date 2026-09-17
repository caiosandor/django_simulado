from django.db import models

class Livro(models.Model):
    TIPO_CHOICES = [
        ('Físico', 'Físico'),
        ('Digital', 'Digital'),
    ]

    CATEGORIA_CHOICES = [
        ('0', '0 – Generalidades e Informação'),
        ('1', '1 – Filosofia e Psicologia'),
        ('2', '2 – Religião e Teologia'),
        ('3', '3 – Ciências Sociais e Direito'),
        ('4', '4 – Linguística e Idiomas'),
        ('5', '5 – Ciências Puras (Exatas e Naturais)'),
        ('6', '6 – Ciências Aplicadas (Tecnologia)'),
        ('7', '7 – Artes e Recreação'),
        ('8', '8 – Literatura'),
        ('9 ', '9– História e Geografia'),
    ]

    titulo = models.CharField(max_length=200, verbose_name="Título")
    autor = models.CharField(max_length=100, verbose_name="Autor")
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='Físico', verbose_name="Tipo de Acervo")
    categoria = models.CharField(max_length=3, choices=CATEGORIA_CHOICES, default='000', verbose_name="Categoria")

    def __str__(self):
        return f"{self.titulo} ({self.tipo})"