# Generated by Django 2.1.2 on 2019-06-23 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_name', models.CharField(max_length=20)),
                ('_comment', models.CharField(max_length=20)),
            ],
        ),
    ]
