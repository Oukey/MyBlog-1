# Generated by Django 3.0.5 on 2020-04-17 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20200417_1803'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={'ordering': ['rating'], 'verbose_name': 'Направление блогов', 'verbose_name_plural': 'Направления блогов'},
        ),
        migrations.AddField(
            model_name='area',
            name='rating',
            field=models.DecimalField(decimal_places=0, default=500, max_digits=8, verbose_name='Рейтинг'),
        ),
    ]
