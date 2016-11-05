from django.db import models

# Create your models here.
class Place(models.Model):
    id = models.AutoField(primary_key=True)
    place_name = models.TextField()
    lat = models.FloatField()
    lng = models.FloatField()
    info = models.TextField()
    place_id = models.TextField()
    group_name = models.CharField(max_length=200)
    capital = models.BooleanField(default=False)
    #img = models.ImageField()
