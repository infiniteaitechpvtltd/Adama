# Generated by Django 4.0.3 on 2022-04-26 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adama_app', '0018_alter_createtask_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createtask',
            name='comment',
            field=models.CharField(max_length=500),
        ),
    ]
