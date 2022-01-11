from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

class Alien(models.Model):
  given_name_of_subject = models.CharField(max_length=124)
  species = models.CharField(max_length=124, default='non-human')
  number_of_apendages = models.IntegerField(default=None)
  number_of_eyes = models.IntegerField(default=None)
  reporter = ForeignKey(get_user_model(), on_delete=models.CASCADE)
  description = models.TextField(max_length=500, default="")
  risk_level = models.IntegerField(default=0)

  def __str__(self):
    return f"{self.given_name}:{self.species}"

  def get_absolute_url(self):
    return reverse('alien_detail', args = [str(self.id)])