# Generated by Django 5.0.1 on 2024-01-11 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user_likes_alter_user_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(blank=True, upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='likes',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
