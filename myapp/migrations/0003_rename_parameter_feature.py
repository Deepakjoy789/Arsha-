# Generated by Django 5.0.3 on 2024-04-02 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_parameter_delete_feature'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Parameter',
            new_name='Feature',
        ),
    ]
