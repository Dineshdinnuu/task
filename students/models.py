from django.db import models

class Student(models.Model):
    student_number = models.IntegerField(primary_key=True) 
    first_name = models.CharField(max_length=30) 
    last_name = models.CharField(max_length=30) 
    email = models.EmailField(max_length=50) 
    field_of_study = models.CharField(max_length=50) 
    gpa = models.FloatField() 


    def __str__(self):
        return self.first_name+' '+self.last_name
