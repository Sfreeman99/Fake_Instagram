# Generated by Django 2.0.1 on 2018-01-31 09:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20180131_0425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='uploaded_by',
            field=models.ForeignKey(
                default='00',
                on_delete=django.db.models.deletion.CASCADE,
                to='app.Profile'),
            preserve_default=False,
        ),
    ]
