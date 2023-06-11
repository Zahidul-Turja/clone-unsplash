from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    user_name = models.CharField(primary_key=True, max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user_name} {self.email}"
