# Generated by Django 3.2.8 on 2021-10-24 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authadoptapp', '0003_auto_20211023_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='dewormer',
            field=models.CharField(default='No Aplica', max_length=300, verbose_name='dewormer'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='diseases_drugs',
            field=models.CharField(default='No Aplica', max_length=300, verbose_name='diseases_drugs'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='vaccines',
            field=models.CharField(default='No Aplica', max_length=300, verbose_name='vaccines'),
        ),
        migrations.AlterField(
            model_name='user',
            name='company',
            field=models.CharField(default='No Aplica', max_length=30, verbose_name='company'),
        ),
        migrations.AlterField(
            model_name='user',
            name='jobs',
            field=models.CharField(default='No Aplica', max_length=30, verbose_name='jobs'),
        ),
    ]
