from django.db import models

# Create your models here.
class QUOTD(models.Model):
    quote = models.TextField()
    said_by = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
