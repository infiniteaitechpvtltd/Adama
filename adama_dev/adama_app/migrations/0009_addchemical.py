# Generated by Django 4.0.3 on 2022-04-21 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adama_app', '0008_batch_card_add_chemical'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddChemical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ChemicalName', models.CharField(max_length=30)),
                ('Percentage', models.CharField(max_length=30)),
                ('QuantityAdded', models.CharField(max_length=30)),
                ('DateTime', models.FloatField(default=0)),
                ('LoadCellStart', models.CharField(max_length=100)),
                ('LoadCellEnd', models.TextField(max_length=5000)),
                ('LoadCellReading', models.TextField(max_length=500)),
                ('Operator', models.CharField(max_length=30)),
            ],
        ),
    ]