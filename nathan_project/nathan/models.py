from django.db import models

class Decades (models.Model):
    name = models.CharField(max_length=100)
    start_year = models.CharField(max_length=100)
    end_year = models.TextField()

class Fads (models.Model):
    
    name = models.CharField(max_length=100)
    image_url = models.TextField()
    description = models.TextField()
    decade = models.ForeignKey(Decades, on_delete=models.CASCADE, related_name='fads')
