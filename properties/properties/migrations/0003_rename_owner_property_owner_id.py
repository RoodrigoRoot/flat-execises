# Generated by Django 4.0.4 on 2022-11-02 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_property_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='owner',
            new_name='owner_id',
        ),
    ]
