from django.db import models


class Categoria(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    class Meta:
        db_table = "categorias"


class Producto(models.Model):
    categoria = models.ForeignKey (Categoria, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.FloatField()
    price = models.FloatField()
    image = models.FileField(upload_to="")

    class Meta:
        db_table = "productos"




