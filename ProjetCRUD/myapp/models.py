from django.db import models

class Fruit(models.Model):
    nom = models.CharField(max_length=100)
    couleur = models.CharField(max_length=100)
    description = models.TextField()

