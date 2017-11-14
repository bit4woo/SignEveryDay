from django.db import models

class task(models.Model):
    task_name = models.CharField(max_length=150)
    request = models.TextField
    starttime = models.DateTimeField
    inter = models.TimeField
    repeat_times = models.IntegerField