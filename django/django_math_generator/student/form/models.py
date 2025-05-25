from django.db import models



class Student(models.Model):
    EducationLevels = [
        ('9-12', 'Some high school'),
        ('12+', 'College'),
     ('12++', 'University')
    ]

    EducationModes = [
        ('<->', 'Regular'),
        ('--->', 'Long-term'),
        ('*', 'Online')
    ]

    Courses = [
        ('math', 'Mathematics'),
        ('phys', 'Physics'),
        ('csit', 'Computer Science'),
        ('eng', 'Literature')
    ]

    name = models.CharField(max_length=20)
    edu_level = models.CharField(choices=EducationLevels)
    edu_mode = models.CharField(choices=EducationModes)
    fav_course = models.CharField(choices=Courses)
