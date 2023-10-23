from django.contrib.auth.models import User
from django.db import models



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'


class Orders(models.Model):
    name: str = models.CharField(max_length=50)
    addition: str = models.TextField()
    sizes: User = models.TextField(max_length=1000)
    material: str = models.CharField(max_length=25)

    price: float = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
