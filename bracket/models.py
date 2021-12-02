from djongo import models

REGIONS = (
    ('east', 'East'),
    ('south', 'South'),
    ('west', 'West'),
    ('midwest', 'Midwest')
)

# Create your models here.
class Bracket(models.Model):
    bracket_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    # list of school objects in the bracket

class School(models.Model):
    name = models.CharField(max_length=100)
    seed = models.IntegerField()
    region = models.CharField(max_length=7, choices=REGIONS)
    is_eliminated = models.BooleanField(default=False)
