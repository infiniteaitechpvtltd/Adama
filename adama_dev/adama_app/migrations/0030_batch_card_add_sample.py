# Generated by Django 4.0.3 on 2022-04-28 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adama_app', '0029_alter_sop_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch_card',
            name='Add_Sample',
            field=models.TextField(default=[''], max_length=1000),
            preserve_default=False,
        ),
    ]
