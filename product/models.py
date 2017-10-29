from django.db import models
from django.core.urlresolvers import reverse


class Flavour(models.Model):
    company = models.CharField(max_length=250)
    flavour_title = models.CharField(max_length=500)
    made_in = models.CharField(max_length=250)
    flavour_image = models.FileField()

    def get_absolute_url(self):
        return reverse('product:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.flavour_title + ' _ ' + self.company


class Name(models.Model):
    flavour = models.ForeignKey(Flavour, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=250)
    name_title = models.CharField(max_length=250)

    def __str__(self):
        return self.name_title
