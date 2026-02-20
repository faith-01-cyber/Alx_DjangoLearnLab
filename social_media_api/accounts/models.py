from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Users that this user is following
    following = models.ManyToManyField(
        'self',
        symmetrical=False,  # one-way follow
        related_name='followers',
        blank=True
    )

    def __str__(self):
        return self.username
