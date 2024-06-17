from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):   #   Note will be a model
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    #   Automatically populate time (No need to ask user)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")    #   related_name is a field on the User to reference its notes

    def __str__(self):
        return self.title