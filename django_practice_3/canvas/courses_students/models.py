from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)

    def __str__(self):
        return f'{self.name}'
    
class Course(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=5000)
    students = models.ManyToManyField(Student, related_name="students")
