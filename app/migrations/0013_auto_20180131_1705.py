# Generated by Django 2.0.1 on 2018-01-31 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20180131_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentmodel',
            old_name='uploaded_by',
            new_name='commentor',
        ),
        migrations.RenameField(
            model_name='imagemodel',
            old_name='commentor',
            new_name='uploaded_by',
        ),
    ]
