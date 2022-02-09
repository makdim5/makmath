from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

from django.contrib.auth.models import User

class Topic(models.Model):
    topic_name = models.CharField(max_length=255, verbose_name="Название темы")
    content = RichTextField(null=True, verbose_name="Текст лекции")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время обновления")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовать")
    section = models.ForeignKey('Section', on_delete=models.PROTECT, null=True, verbose_name="Выбор раздела")
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)

    def get_absolute_url(self):
        return reverse('topic', kwargs={'topic_slug': self.slug})

    def __str__(self):
        return self.topic_name

    class Meta:
        verbose_name = 'Темы'
        verbose_name_plural = 'Темы'
        ordering = ['section', 'time_create']


class Section(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название раздела")
    image_link = models.TextField(null=True, verbose_name="URL картинки")
    description = models.TextField(max_length=100, null=True, verbose_name="Описание")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовать")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('section', kwargs={'section_slug': self.slug})

    class Meta:
        verbose_name = 'Разделы'
        verbose_name_plural = 'Разделы'


class Task(models.Model):
    task_info = models.TextField(max_length=255,null=True, verbose_name="Задание")
    correct_answer = models.CharField(max_length=5, null=True, verbose_name="Правильный ответ")
    topic = models.ForeignKey('Topic', on_delete=models.PROTECT, null=True, verbose_name="Выбор темы")

    def __str__(self):
        return self.task_info

    class Meta:
        verbose_name = 'Задания'
        verbose_name_plural = 'Задания'
        ordering = ['topic']

    def check_task(self, answer):
        return answer == self.correct_answer


class TaskComplition(models.Model):
    task = models.ForeignKey('Task', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)