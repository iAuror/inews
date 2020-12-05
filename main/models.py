from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Оглавление')
    content = models.TextField(verbose_name='Новость')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    published = models.BooleanField(verbose_name='Опубликованно', default=False)
    editor = models.ManyToManyField(User, related_name='editor')
    author = models.ForeignKey('Authors', on_delete=models.CASCADE, verbose_name='Автор статьи')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категории', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Authors(models.Model):
    name = models.CharField(max_length=200, verbose_name='Автор')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
