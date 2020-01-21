from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Privado"),
    (1, "Publico")
)


class Post(models.Model):
    objects = None
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tittle = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = [
            '-created_on'
        ]

    def __str__(self):
        return self.tittle


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = [
            '-created_on'
        ]

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    nick_name = models.CharField(max_length=12, unique=True, default=None)

    def __str__(self):
        return self.user.username
