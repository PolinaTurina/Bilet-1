# Generated by Django 4.2.1 on 2023-06-24 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d/', verbose_name='Изображение'),
        ),
    ]
