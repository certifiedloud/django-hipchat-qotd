from django.db import models


class QOTD(models.Model):
    quote = models.TextField(unique=True)
    said_by = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Quotes"

    def __str__(self):
        return self.quote[0:30]
