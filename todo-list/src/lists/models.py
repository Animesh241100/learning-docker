from django.db import models
import datetime


class Task(models.Model):
    name = models.CharField(max_length=32)
    is_completed = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.time_updated = datetime.datetime.now()
        super(Task, self).save(*args, **kwargs)
