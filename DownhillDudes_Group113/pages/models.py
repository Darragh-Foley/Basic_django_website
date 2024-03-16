from django.db import models

# Create your models here.
class Trail(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField(upload_to='static/images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    trail = models.ForeignKey(Trail, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.trail.name} - {self.rating}"
    
class MagicPage(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title