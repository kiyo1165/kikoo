from django.db import models
from django.utils import timezone #ツイートした日付
from django.contrib.auth.models import User #user登録


class Post(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) #一対多
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.ImageField(default=0)
    disliks = models.ImageField(default=0)

    def __str__(self):
        return self.content
