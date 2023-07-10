# Generated by Django 4.0.3 on 2022-05-05 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adama_app', '0038_rename_bottle_tetsing_packagecard_bottle_testing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='batch_card',
            old_name='Date',
            new_name='Created_Date',
        ),
        migrations.RenameField(
            model_name='packagecard',
            old_name='Chemical_name',
            new_name='Brand_name',
        ),
        migrations.RemoveField(
            model_name='batch_card',
            name='AllotedOperator',
        ),
        migrations.AddField(
            model_name='batch_card',
            name='Approved_By',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='batch_card',
            name='Approved_Date',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='batch_card',
            name='Created_By',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='batch_card',
            name='Plant_Name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='chemical',
            name='Base_Calc',
            field=models.CharField(default='Batch_Size', max_length=30),
        ),
        migrations.AddField(
            model_name='chemical',
            name='Type',
            field=models.CharField(default='Liquid', max_length=30),
        ),
        migrations.AddField(
            model_name='packagecard',
            name='Approved_By',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='packagecard',
            name='Approved_Date',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='batch_card',
            name='Add_Sample',
            field=models.TextField(default='[]', max_length=1000),
        ),
    ]