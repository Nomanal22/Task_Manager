# Generated by Django 5.0 on 2023-12-31 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_rename_is_completed_task_completed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='creation_date_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='photos',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]