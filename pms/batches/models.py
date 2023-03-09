from django.db import models
# Create your models here.

genderchoice=(('Male','Male'),('Female','Female'))

class faculty(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    passwors=models.CharField(max_length=10)
    gender=models.CharField(choices=genderchoice,max_length=100)

    def __str__(self):
        return self.name
    
    class meta:
        db_table='Faculty'

class subjects(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class meta:
        db_table='Subjects'

class batches(models.Model):
    name=models.CharField(max_length=50)
    faculty=models.ForeignKey(faculty, on_delete=models.CASCADE)
    subjects=models.ForeignKey(subjects, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class meta:
        db_table='Batches'
