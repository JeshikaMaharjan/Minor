# Generated by Django 4.1.3 on 2023-01-27 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0006_remove_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default=0, upload_to='images'),
            preserve_default=False,
        ),
    ]