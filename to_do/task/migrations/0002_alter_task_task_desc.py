# Generated by Django 4.1.5 on 2023-02-19 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_desc',
            field=models.TextField(blank=True),
        ),
    ]
