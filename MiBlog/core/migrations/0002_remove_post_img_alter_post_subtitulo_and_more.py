# Generated by Django 4.1.7 on 2023-04-13 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img',
        ),
        migrations.AlterField(
            model_name='post',
            name='subtitulo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
    ]
