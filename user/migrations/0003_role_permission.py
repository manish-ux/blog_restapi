# Generated by Django 3.2.7 on 2022-06-24 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('user', '0002_auto_20220624_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='permission',
            field=models.ManyToManyField(blank=True, to='auth.Permission'),
        ),
    ]