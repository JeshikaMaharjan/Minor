# Generated by Django 4.1.3 on 2023-01-16 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fee',
            name='admissionFee',
            field=models.FloatField(default=1),
        ),
    ]