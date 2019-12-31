from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    created_date = models.DateField(default=timezone.now, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    completed_date = models.DateField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def _str_(self):
        return self.title
