from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title=models.CharField(max_length=100)
    description= models.CharField(max_length=250)
    url= models.URLField(blank=True)
    image=models.ImageField(upload_to='portfolio/images/')

    def __str__(self):
        return self.title
