from django.db import models

class Portfolio(models.Model):
    stock = models.CharField(max_length=10)
    quantity = models.IntegerField()
    price = models.DecimalField(...,decimal_places=5, max_digits=10)
    
    
    def __str__(self):
        return self.stock
    

