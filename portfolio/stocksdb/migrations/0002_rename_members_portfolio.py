# Generated by Django 3.2 on 2021-04-28 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocksdb', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Members',
            new_name='Portfolio',
        ),
    ]