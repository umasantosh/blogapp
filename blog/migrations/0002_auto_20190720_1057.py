# Generated by Django 2.2.2 on 2019-07-20 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='slog',
            new_name='slug',
        ),
    ]
