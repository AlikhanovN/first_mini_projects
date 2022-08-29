from django.db import models

# Create your models here.
class Games(models.Model):
    title = models.CharField(max_length=222)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="media/%Y/%m/%d")
    content = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title}, {self.content}, {self.created}, {self.image}"

    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"
        ordering = ["-id", ]