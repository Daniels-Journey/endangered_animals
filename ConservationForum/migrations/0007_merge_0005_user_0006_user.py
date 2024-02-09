# Generated by Django 5.0.1 on 2024-02-09 03:58

from django.db import migrations


def revert_migration_0005(apps, schema_editor):
    # Write code here to revert changes made in migration 0005
    pass


def revert_migration_0006(apps, schema_editor):
    # Write code here to revert changes made in migration 0006
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('ConservationForum', '0006_user'),
        ('ConservationForum', '0005_user'),
    ]

    operations = [
        migrations.RunPython(revert_migration_0006, migrations.RunPython.noop),
        migrations.RunPython(revert_migration_0005, migrations.RunPython.noop),
    ]