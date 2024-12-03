from django.db import models

class Cars(models.Model):
    name = models.CharField(max_length=100)
    model = models.TextField()
    year = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




