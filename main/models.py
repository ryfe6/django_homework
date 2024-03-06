from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    """product model работает с продуктами"""
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    img = models.ImageField(upload_to='poducts/', verbose_name='Фотография', **NULLABLE)
    category = models.ForeignKey("Category", related_name='Products', verbose_name="Категория",
                                 on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateField(verbose_name='Дата создания')
    updated_at = models.DateField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    """category model работает с категориями товаров"""
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
