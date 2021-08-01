from django.db import models
from datetime import date


class News(models.Model):
    name = models.CharField('Название', max_length=155)
    url = models.SlugField('Url', unique=True, max_length=120)
    description = models.TextField('Описание')
    date = models.DateField('Дата', blank=True, default=date.today)
    photo = models.ImageField('Фото', upload_to='news/', blank=True, null=True)

    def __str__(self):
        return f'{self.name} {str(self.date)}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class License(models.Model):
    name = models.CharField('Название', max_length=150)
    photo = models.ImageField('Фото', upload_to='license/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Лицензия'
        verbose_name_plural = 'Лицензии'


class Category(models.Model):
    name = models.CharField('Название', max_length=155, unique=True)
    parent_id = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, verbose_name='Родитель',
                                  related_name="children")
    description = models.TextField('Описание', blank=True, null=True)
    url = models.SlugField('Url', unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Service(models.Model):
    name = models.CharField('Название', max_length=155)
    price = models.DecimalField('Цена', max_digits=12, decimal_places=2)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)

    def __str__(self):
        return f'Название - {self.name}, цена - {str(self.price)}, категория - {self.category}'

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class CompanyType(models.Model):
    name = models.CharField('Название', max_length=150, unique=True)
    url = models.SlugField(max_length=155, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип компании'
        verbose_name_plural = 'Типы компаний'


class Company(models.Model):
    name = models.CharField('Название', max_length=150, unique=True)
    type = models.ForeignKey(CompanyType, verbose_name='Тип', on_delete=models.CASCADE)

    def __str__(self):
        return f'Название - {self.name}, тип - {self.type}'

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

