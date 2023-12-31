# Generated by Django 4.0.3 on 2022-05-05 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adama_app', '0039_rename_date_batch_card_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch_card',
            name='Base_Calc',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='batch_card',
            name='Add_Chemical',
            field=models.TextField(default='[]', max_length=10000),
        ),
        migrations.AlterField(
            model_name='batch_card',
            name='Chemical_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='batch_card',
            name='Expiry',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='batch_card',
            name='Expiry_Date',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='batch_card',
            name='MFG_Date',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='batch_card',
            name='Raw_Materials',
            field=models.TextField(default='[]', max_length=5000),
        ),
        migrations.AlterField(
            model_name='batch_card',
            name='Remark',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='batch_card',
            name='Technicals',
            field=models.TextField(default='[]', max_length=500),
        ),
    ]
