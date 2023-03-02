from django.db import models

# Create your models here.
class employees(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Password=models.CharField(max_length=10)
    age=models.PositiveIntegerField()
    salary=models.FloatField()
    Joining_Date=models.DateField()

    Created_at=models.DateTimeField(auto_now_add=True)
    Upadate_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name
    
    class meta:
        db_table='Employees'


class product(models.Model):
    pName=models.CharField(max_length=100)
    pDescription=models.CharField(max_length=100)
    pColor=models.CharField(max_length=20)
    pPrice=models.FloatField()
    pQuantity=models.PositiveIntegerField()
    pAvalibility=models.BooleanField(default=True)
     
    Last_Updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pName
    
    class meta:
        db_table='Product'