# Generated by Django 4.0.3 on 2023-01-02 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adama_app', '0045_packagecard_productioncount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='packagecard',
            old_name='nozzle_one',
            new_name='bpm',
        ),
    ]
