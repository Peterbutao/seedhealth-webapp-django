# Generated by Django 4.0.3 on 2022-03-26 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plantdiseasemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('symptoms', models.CharField(max_length=200)),
                ('causativeagent', models.CharField(max_length=200)),
                ('causativeorganism', models.CharField(max_length=200)),
                ('modeofspread', models.CharField(max_length=200)),
                ('organsaffected', models.CharField(max_length=200)),
                ('cropsaffected', models.CharField(max_length=200)),
                ('planttypesaffected', models.CharField(max_length=200)),
                ('pathogengeneration', models.CharField(max_length=200)),
                ('geographicdistribution', models.CharField(max_length=200)),
                ('prevention', models.CharField(max_length=200)),
                ('control', models.CharField(max_length=200)),
            ],
        ),
    ]
 