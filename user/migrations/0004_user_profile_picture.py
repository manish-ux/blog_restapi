# Generated by Django 3.2.7 on 2022-06-26 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_role_permission'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
