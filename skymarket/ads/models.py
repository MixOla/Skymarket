from django.conf import settings


from django.core.validators import MinLengthValidator
from django.db import models
from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=200, null=True)
    price = models.PositiveIntegerField(null=True)
    image = models.ImageField(upload_to="ad_images", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ["created_at"]


    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.CharField(max_length=1000, null=True)
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE, null=True)
    ad = models.ForeignKey(Ad, verbose_name="Объявление", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


    def __str__(self):
        return self.text

