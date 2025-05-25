from django.db import models
from django.db.models import Q

class User(models.Model):
    username = models.CharField(max_length=100)
    age = models.IntegerField()
    access_level = models.CharField(max_length=20)

    class Meta:
        constraints = [
            models.CheckConstraint(
                age = Q(age__gte=13),
                access_level = Q(access_level__in=['admin', 'moderator', 'user'])
            )
        ]