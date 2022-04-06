from django.db import models

class Plantdiseasemodel(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    symptoms = models.CharField(max_length=200)
    causativeagent = models.CharField(max_length=200)
    causativeorganism = models.CharField(max_length=200)
    modeofspread = models.CharField(max_length=200)
    organsaffected = models.CharField(max_length=200)
    cropsaffected = models.CharField(max_length=200)
    planttypesaffected = models.CharField(max_length=200)
    pathogengeneration = models.CharField(max_length=200)
    geographicdistribution = models.CharField(max_length=200)
    prevention = models.CharField(max_length=200)
    control = models.CharField(max_length=200)