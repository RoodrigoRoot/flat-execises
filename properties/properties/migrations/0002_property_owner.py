# Generated by Django 4.0.4 on 2022-11-02 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='owner',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]