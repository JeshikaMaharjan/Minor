# Generated by Django 4.1.3 on 2022-12-25 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('role', models.IntegerField(max_length=1)),
                ('fees', models.FloatField(null=True)),
            ],
        ),
    ]