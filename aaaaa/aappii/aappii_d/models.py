from django.db import models
import uuid

class arrr(models.Model):
    token = models.CharField(max_length=255, unique=True)
    key = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
