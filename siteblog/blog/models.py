from django.db import models
from django.urls import reverse

'''
POST
==========
title, slug, content, posted_by, created_at, photo, category, tags, views

CATEGORY
============
title, slug

TAGS
==========
title, slug
'''


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(max_length=100, verbose_name='Url категории', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Имя тега')
    slug = models.SlugField(max_length=50, verbose_name='Url тега', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, verbose_name='Url поста', unique=True)
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateField(auto_now_add=True, verbose_name='Опубликовано')
    posted_by = models.CharField(max_length=255, verbose_name='Автор')
    photo = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts', verbose_name='Категория  ')
    tag = models.ManyToManyField(Tag, blank=True, related_name='posts')
    views = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
