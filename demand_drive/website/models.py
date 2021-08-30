from django.db import models
from django.utils import timezone

from django.urls import reverse
# Create your models here.
class Demand(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
   
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('demand-detail', kwargs={'pk': self.pk})