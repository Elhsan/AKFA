from django.db import models




class Order(models.Model):
    имя = models.CharField(max_length=100)
    размеры = models.CharField(max_length=10)
    стоимость = models.IntegerField()
    материал = models.CharField(max_length=250)

    def __str__(self):
        return self.имя

    
    def get_absolute_url(self):
        return f'/news/{self.id}'
    