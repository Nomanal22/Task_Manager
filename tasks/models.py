from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField(null=True)
    photos = models.ImageField(null=True)
    creation_date_time = models.DateTimeField(null=True)
    priority = models.Avg()
    completed = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title
