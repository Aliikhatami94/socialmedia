from django.db import models


class Tweet(models.Model):
    text = models.CharField(max_length=200)
    public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']


class Feedback(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    like = models.BooleanField(default=False)
