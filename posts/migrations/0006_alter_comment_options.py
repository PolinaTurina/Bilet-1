# Generated by Django 4.2.1 on 2023-06-29 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-create_date'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
    ]
