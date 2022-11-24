# Generated by Django 4.1.3 on 2022-11-24 08:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0050_alter_preprocedurecard_admission_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrumentused',
            name='table_ca2',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='instrumentused',
            name='table_ca3',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='instrumentused',
            name='table_ca4',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='preprocedurecard',
            name='admission_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 24, 8, 3, 37, 488017, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='preprocedurecard',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 24, 8, 3, 37, 488017, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='preprocedurecard',
            name='sign_date',
            field=models.DateField(default=datetime.datetime(2022, 11, 24, 8, 3, 37, 488017, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='surgicalproceduraldetail',
            name='console_end_time',
            field=models.TimeField(default=datetime.datetime(2022, 11, 24, 8, 3, 37, 490016, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='surgicalproceduraldetail',
            name='console_start_time',
            field=models.TimeField(default=datetime.datetime(2022, 11, 24, 8, 3, 37, 490016, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='surgicalproceduraldetail',
            name='docking_begins',
            field=models.TimeField(default=datetime.datetime(2022, 11, 24, 8, 3, 37, 490016, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='surgicalproceduraldetail',
            name='docking_ends',
            field=models.TimeField(default=datetime.datetime(2022, 11, 24, 8, 3, 37, 490016, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='surgicalproceduraldetail',
            name='surg_end_time',
            field=models.TimeField(default=datetime.datetime(2022, 11, 24, 8, 3, 37, 490016, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='surgicalproceduraldetail',
            name='surg_start_time',
            field=models.TimeField(default=datetime.datetime(2022, 11, 24, 8, 3, 37, 490016, tzinfo=datetime.timezone.utc)),
        ),
    ]
