from django.db import models


class Content(models.Model):
    content = models.CharField(max_length=1000, verbose_name="Content")
    user = models.CharField(max_length=25, verbose_name="User name")
    date_added = models.DateTimeField(auto_now=True, verbose_name="Date added")

    class Meta:
        ordering = ("date_added",)
