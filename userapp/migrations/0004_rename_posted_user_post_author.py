# Generated by Django 4.0.3 on 2022-03-18 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_alter_userprofile_user_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='posted_user',
            new_name='author',
        ),
    ]
