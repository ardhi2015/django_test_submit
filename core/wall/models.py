from core.service.models import User
from django.db import models


class TimestampModel(models.Model):
    """
    Abstract model that provides created and updated timestamps
    """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class WallPost(TimestampModel):
    """
    Wall post
    """

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        managed = True


class WallLikes(TimestampModel):
    """
    Wall likes
    """

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    wall_post = models.ForeignKey(WallPost, on_delete=models.CASCADE)

    class Meta:
        managed = True
