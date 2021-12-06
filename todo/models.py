from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(blank=True, max_length=100)
    date = models.DateField(auto_now=True)
    complete = models.BooleanField()
    task_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title
