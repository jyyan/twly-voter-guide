from django.db import models


class Committees(models.Model):
    members = models.ManyToManyField('legislator.Legislator', through='Legislator_Committees')
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

class Legislator_Committees(models.Model):
    legislator = models.ForeignKey('legislator.Legislator', to_field="uid")
    committee = models.ForeignKey(Committees)
    ad = models.IntegerField()
    session = models.IntegerField()
    chair = models.BooleanField()
