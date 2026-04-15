from django.db import models

from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to='categories/', blank=True, null=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('module_project:category_detail', args=[str(self.id)])


class Discipline(models.Model):
    DIFFICULTY_CHOICES = [
        ('beginner', 'Начальный'),
        ('intermediate', 'Средний'),
        ('advanced', 'Продвинутый'),
    ]

    name = models.CharField(max_length=100, verbose_name="Название")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='disciplines',
        verbose_name="Категория"
    )
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to='disciplines/', blank=True, null=True, verbose_name="Изображение")
    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
        default='beginner',
        verbose_name="Сложность"
    )
    is_olympic = models.BooleanField(default=False, verbose_name="Олимпийский вид")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    

    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    def get_absolute_url(self):
        return reverse('module_project:discipline_detail', args=[str(self.id)])

