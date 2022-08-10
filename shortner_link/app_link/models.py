from django.db import models


class Users(models.Model):
    name_users = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

    def __str__(self):
        return self.name_users


class LinkInfo(models.Model):
    original_link = models.CharField(max_length=10000)
    short_link = models.CharField(max_length=15)

    def __str__(self):
        return self.short_link


class Post(models.Model):
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    text = models.TextField()
