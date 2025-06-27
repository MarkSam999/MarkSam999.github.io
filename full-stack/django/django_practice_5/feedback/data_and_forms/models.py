from django.db import models
from django.db.models import Q

class Feedback(models.Model):
    name  = models.CharField(max_length=100, blank=False)
    email = models.EmailField()
    rating = models.IntegerField()
    message = models.TextField(max_length=500, blank=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check = Q(rating__lte=6),
                name = "less_than_6"
            ), 
            models.CheckConstraint(
                check = Q(rating__gte=0),
                name = "more_than_0"
            ), 
        ]
