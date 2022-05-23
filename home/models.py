from django.db import models


class Feedback(models.Model):
    name = models.TextField(max_length=200)
    user_email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=1024)

    def __str__(self) -> str:
        return str(self.name)
