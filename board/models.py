from django.db import models
from django.contrib.auth.models import User


class Story(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=1)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="stories"
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "stories"

    def __str__(self):
        return f"{self.title}"


class Vote(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE,
                              related_name="votes")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name="votes")

    def save(self, *args, **kwargs):
        self.story.score = self.story.score + 1
        self.story.save()

        super(Vote, self).save(*args, **kwargs)


class Comment(models.Model):
    message = models.TextField()
    story = models.ForeignKey(Story, on_delete=models.CASCADE,
                              related_name="comments")
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    created_at = models.DateTimeField(auto_now_add=True)
