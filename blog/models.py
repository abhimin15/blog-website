from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=25)
    author=models.CharField(max_length=15)
    date=models.CharField(max_length=15)
    body=models.CharField(max_length=500)
    logo=models.FileField()
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk' : self.pk})
    def __str__(self):
        return self.title+'-'+self.author


