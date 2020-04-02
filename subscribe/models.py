from django.db import models

class Subscription(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.name