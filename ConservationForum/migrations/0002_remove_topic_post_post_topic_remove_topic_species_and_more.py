# Generated by Django 5.0.1 on 2024-02-01 01:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConservationForum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ConservationForum.topic'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='topic',
            name='species',
        ),
        migrations.AddField(
            model_name='topic',
            name='species',
            field=models.ManyToManyField(to='ConservationForum.species'),
        ),
    ]
