from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Ürün Adı", help_text="Ürün adını yazınız")
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="products/%Y/%m/%d/", default="")
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
# Create your models here.

    def __str__(self):
        return self.name
