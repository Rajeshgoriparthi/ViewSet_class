from django.db import models

# Create your models here.


class Product_catagiry(models.Model):
    pc_id=models.IntegerField()
    pc_name=models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.pc_name
    
class Product(models.Model):
    pc_id=models.ForeignKey(Product_catagiry,on_delete=models.CASCADE)
    pid=models.IntegerField()
    name=models.CharField(max_length=30)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    date=models.DateField()
    
    def __str__(self):
        return self.name
    