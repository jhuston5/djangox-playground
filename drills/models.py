from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

class Drill(models.Model):
  drill_date = models.DateTimeField(blank=True, null=True)
  soldier = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  location = models.CharField(max_length=64)
  description = models.TextField(default='')

  def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.description

  def get_absolute_url(self):
    return reverse('drill_detail', args=[str(self.id)])