from django.db import models

class Task(models.Model):
    # Yêu cầu đề bài: title (required), is_done (default false)
    title = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title