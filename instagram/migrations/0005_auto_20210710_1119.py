# Generated by Django 2.1 on 2021-07-10 08:19

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_auto_20210710_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phoneNumber',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profilePic',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
