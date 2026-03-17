from django.db import models
from base.models import BaseModel

class Certification(BaseModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name