# Generated by Django 4.2 on 2023-04-25 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClientsExistants',
            new_name='ClientPotentiel',
        ),
        migrations.RenameModel(
            old_name='ClientPotentiels',
            new_name='ClientsExistant',
        ),
        migrations.RenameModel(
            old_name='Sales',
            new_name='Sale',
        ),
    ]