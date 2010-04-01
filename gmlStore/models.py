from django.db import models

# Create your models here.
class Annotation(models.Model):
  gml = models.XMLField()
  creation_date = models.DateTimeField('date created')
