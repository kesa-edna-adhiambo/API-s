# Generated by Django 5.0.7 on 2024-09-16 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
        ('users', '0003_alter_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping',
            name='users',
            field=models.ManyToManyField(to='users.user'),
        ),
    ]
