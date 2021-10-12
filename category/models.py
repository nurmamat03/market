from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural='Категории'

        def __str__(self):
            return self.title


