# Generated by Django 4.1 on 2022-09-26 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='market',
            old_name='forms',
            new_name='options',
        ),
    ]
