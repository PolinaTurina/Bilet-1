# Generated by Django 4.2.1 on 2023-06-24 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='img',
            new_name='image',
        ),
    ]
