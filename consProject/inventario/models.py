from django.db import models

class Producto(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.FloatField()
    image = models.FileField(upload_to="")

    class Meta:
        db_table = "productos"




