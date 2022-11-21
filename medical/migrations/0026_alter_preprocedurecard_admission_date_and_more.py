# Generated by Django 4.1.3 on 2022-11-20 22:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0025_alter_preprocedurecard_admission_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preprocedurecard',
            name='admission_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 20, 22, 36, 38, 861845, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='preprocedurecard',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 20, 22, 36, 38, 861845, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='preprocedurecard',
            name='sign_date',
            field=models.DateField(default=datetime.datetime(2022, 11, 20, 22, 36, 38, 861845, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='GastrointestinalProcedure',
            fields=[
                ('gastro_procedure_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_surgeon', models.CharField(default=' ', max_length=40)),
                ('second_surgeon', models.CharField(default=' ', max_length=40)),
                ('cholecystectomy', models.CharField(default=' ', max_length=80)),
                ('bariatric', models.CharField(default=' ', max_length=80)),
                ('esophageal', models.CharField(default=' ', max_length=80)),
                ('gastric', models.CharField(default=' ', max_length=80)),
                ('hemicolectomy', models.CharField(default=' ', max_length=80)),
                ('liver_surgery', models.CharField(default=' ', max_length=80)),
                ('hernia_unilateral', models.CharField(default=' ', max_length=80)),
                ('hernia_bilateral', models.CharField(default=' ', max_length=80)),
                ('ventral_hernia', models.CharField(default=' ', max_length=80)),
                ('fundoplication', models.CharField(default=' ', max_length=80)),
                ('sigmoid_resection', models.CharField(default=' ', max_length=80)),
                ('rectal', models.CharField(default=' ', max_length=80)),
                ('esophagus_implants', models.CharField(default=' ', max_length=80)),
                ('linx_implants', models.CharField(default=' ', max_length=80)),
                ('other', models.CharField(default=' ', max_length=80)),
                ('card_id', models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='medical.card')),
            ],
        ),
    ]