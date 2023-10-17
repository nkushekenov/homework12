from django.db import models

class ExampleModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
