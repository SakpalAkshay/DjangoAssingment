from django.db import models


class UserDetails(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=12, blank=True)

    class Meta:
        verbose_name = "User Detail"
        verbose_name_plural = "User Details"

    def __str__(self):
        return self.username
