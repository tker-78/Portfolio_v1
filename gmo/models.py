from django.db import models

# Create your models here.

class KLine(models.Model):
    time = models.DateTimeField(primary_key=True)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()

    class Meta:
        verbose_name_plural = 'KLine'
