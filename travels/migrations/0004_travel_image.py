# Generated by Django 3.2.9 on 2022-03-09 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0003_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='image',
            field=models.ImageField(null=True, upload_to='travels'),
        ),
    ]
