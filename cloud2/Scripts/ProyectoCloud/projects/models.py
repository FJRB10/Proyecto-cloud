import email
import uuid
from email.policy import default
from enum import unique
from operator import truediv
from unicodedata import name
from django.db import models

# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length = 200)
    document = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)
    email = models.TextField(null = True, blank = True)

def __str__(self):
    return self.name