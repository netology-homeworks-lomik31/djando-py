from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    image = models.URLField()
    release_date = models.DateField()
    lte_exists  = models.BooleanField()
    slug = models.SlugField()
