# Generated by Django 4.2 on 2023-04-28 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_alter_contract_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contract',
            options={'permissions': (('can modify contract', 'can modify is own contracts'),)},
        ),
    ]
