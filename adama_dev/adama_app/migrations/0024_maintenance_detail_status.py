# Generated by Django 4.0.3 on 2022-04-26 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adama_app', '0023_maintenance_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenance_detail',
            name='status',
            field=models.CharField(default='NA', max_length=30),
            preserve_default=False,
        ),
    ]