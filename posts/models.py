from django.db import models


class Post(models.Model):
    title=models.CharField(max_length=50, verbose_name="Заголовок")
    text=models.TextField(blank=False, verbose_name="Текст")
    image=models.ImageField(upload_to="%Y/%m/%d/", verbose_name="Изображение", blank=True, null=True)
    create_date=models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-create_date"]

    def __str__(self):
        return self.title