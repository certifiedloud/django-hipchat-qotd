from django.db import models


class QOTD(models.Model):
    quote = models.TextField()
    said_by = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s...' % (self.quote[0:30])
