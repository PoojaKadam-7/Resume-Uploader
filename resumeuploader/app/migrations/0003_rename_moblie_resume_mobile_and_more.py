# Generated by Django 4.0.6 on 2022-10-18 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_resume_pin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='moblie',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='resume',
            old_name='Profile_image',
            new_name='profile_image',
        ),
    ]
