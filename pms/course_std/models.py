from django.db import models

# Create your models here.

class course(models.Model):
    name=models.CharField(max_length=50)
    duration=models.CharField(max_length=200)
    fees=models.IntegerField()

    def __str__(self):
        return self.name
    
    class meta:
     db_table='Courses'


class std(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    standard=models.IntegerField()

    def __str__(self):
     return self.name
    
    class meta:
     db_table='Student'




