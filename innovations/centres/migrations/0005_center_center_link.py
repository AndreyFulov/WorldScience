# Generated by Django 3.1.7 on 2021-03-14 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centres', '0004_auto_20210314_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='center',
            name='center_link',
            field=models.TextField(default='google.com'),
        ),
    ]
