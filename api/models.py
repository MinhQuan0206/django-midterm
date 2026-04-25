from django.db import models


class Note(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


class Task(models.Model):
    title = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
