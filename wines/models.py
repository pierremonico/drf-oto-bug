from django.db import models


class Bottle(models.Model):
    name = models.CharField(max_length=140)


class Cork(models.Model):
    name = models.CharField(max_length=140)
    bottle = models.OneToOneField(
        to=Bottle,
        on_delete=models.SET_NULL,
        related_name="cork",
        blank=True, null=True
    )
