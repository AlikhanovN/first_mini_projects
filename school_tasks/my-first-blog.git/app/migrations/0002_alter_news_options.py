# Generated by Django 4.1 on 2022-08-29 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-id'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]
