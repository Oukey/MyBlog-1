from django.db import models


class Area(models.Model):
    name = models.CharField(max_length=100, verbose_name="Направление")
    slug = models.SlugField(max_length=200, db_index=True, unique=True, default=None)
    rating = models.DecimalField(verbose_name='Рейтинг', max_digits=8, decimal_places=0, default=500)

    class Meta:
        verbose_name_plural = "Направления блогов"
        verbose_name = "Направление блогов"
        ordering = ['rating']

    def __str__(self):
        return self.name


class GroupKnowledge(models.Model):
    name = models.CharField(max_length=100, verbose_name="Тема")
    slug = models.SlugField(max_length=200, db_index=True, unique=True,  default=None)
    area_kn = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True, verbose_name='Направление')
    rating = models.DecimalField(verbose_name='Рейтинг', max_digits=8, decimal_places=0, default=500)

    class Meta:
        verbose_name_plural = "Темы"
        verbose_name = "Тема"
        ordering = ['rating']

    def __str__(self):
        return self.name
