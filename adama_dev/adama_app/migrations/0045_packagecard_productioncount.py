# Generated by Django 4.0.3 on 2022-09-26 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adama_app', '0044_alter_notifications_db_admin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='packagecard',
            name='ProductionCount',
            field=models.IntegerField(default=0),
        ),
    ]
