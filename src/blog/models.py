from django.db import models
from django.urls import reverse

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)
    author = models.TextField(blank=True, null=False)

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"id": self.id})
