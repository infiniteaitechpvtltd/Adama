# Generated by Django 4.0.3 on 2022-04-25 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adama_app', '0016_rename_task_tasks_list_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createtask',
            old_name='date',
            new_name='completed_date',
        ),
        migrations.AddField(
            model_name='createtask',
            name='created_date',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='createtask',
            name='shift',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
