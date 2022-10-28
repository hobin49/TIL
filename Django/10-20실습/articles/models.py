from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField

# Create your models here.
# 회원가입할때
class User(AbstractUser):
    pass


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to="articles/")
    thumbnail = ProcessedImageField(
        blank=True,
        processors=[Thumbnail(200, 300)],
        format="JPEG",
        options={"quality": 90},
    )


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=80)
