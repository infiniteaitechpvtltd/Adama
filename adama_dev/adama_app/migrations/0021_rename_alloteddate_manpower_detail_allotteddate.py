# Generated by Django 4.0.3 on 2022-04-26 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adama_app', '0020_manpower_detail_plant_detail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manpower_detail',
            old_name='AllotedDate',
            new_name='AllottedDate',
        ),
    ]
