# Generated by Django 3.0.5 on 2020-04-17 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_remove_subgroupknowledge_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={'ordering': ['name'], 'verbose_name': 'Направление блогов', 'verbose_name_plural': 'Направления блогов'},
        ),
        migrations.AlterModelOptions(
            name='groupknowledge',
            options={'ordering': ['name'], 'verbose_name': 'Тема', 'verbose_name_plural': 'Темы'},
        ),
        migrations.AlterField(
            model_name='area',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Направление блога'),
        ),
        migrations.AlterField(
            model_name='groupknowledge',
            name='area_kn',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blogapp.Area', verbose_name='Направление'),
        ),
        migrations.AlterField(
            model_name='groupknowledge',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Тема'),
        ),
        migrations.DeleteModel(
            name='SubGroupKnowledge',
        ),
    ]
