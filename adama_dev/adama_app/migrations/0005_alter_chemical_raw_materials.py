# Generated by Django 4.0.3 on 2022-04-19 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adama_app', '0004_batch_card_mfg_date_batch_card_shiftname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chemical',
            name='Raw_Materials',
            field=models.CharField(max_length=10000),
        ),
    ]
