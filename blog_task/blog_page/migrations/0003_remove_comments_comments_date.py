# Generated by Django 2.1.2 on 2019-06-23 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_page', '0002_auto_20190624_0011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comments_date',
        ),
    ]
