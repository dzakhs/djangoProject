from django.db import models
from mailling_list.models import NULLABLE

class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержимое статьи', **NULLABLE)
    image = models.ImageField(upload_to='blog/media/', verbose_name='изображение', **NULLABLE)
    views = models.IntegerField(default=0, verbose_name='количество просмотров')
    publish_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ('views',)