# Generated by Django 3.0 on 2019-12-17 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20191214_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cattle',
            name='image',
            field=models.ImageField(default='https://picsum.photos/600', upload_to='', verbose_name='Image'),
        ),
    ]
