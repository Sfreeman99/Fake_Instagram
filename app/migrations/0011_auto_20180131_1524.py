# Generated by Django 2.0.1 on 2018-01-31 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20180131_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='uploaded_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Profile'),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='uploaded_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Profile'),
        ),
    ]
