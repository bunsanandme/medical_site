# Generated by Django 4.1.3 on 2022-11-22 20:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0035_alter_preprocedurecard_admission_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roboticarmlocation',
            old_name='roboric_arm_loc_id',
            new_name='robotic_arm_loc_id',
        ),
        migrations.AlterField(
            model_name='preprocedurecard',
            name='admission_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 22, 20, 24, 11, 431590, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='preprocedurecard',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 22, 20, 24, 11, 431590, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='preprocedurecard',
            name='sign_date',
            field=models.DateField(default=datetime.datetime(2022, 11, 22, 20, 24, 11, 431590, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='surgicalproceduraldetail',
            name='console_end_time',
            field=models.TimeField(default=datetime.datetime(2022, 11, 22, 20, 24, 11, 434580, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='surgicalproceduraldetail',
            name='console_start_time',
            field=models.TimeField(default=datetime.datetime(2022, 11, 22, 20, 24, 11, 434580, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='surgicalproceduraldetail',
            name='docking_begins',
            field=models.TimeField(default=datetime.datetime(2022, 11, 22, 20, 24, 11, 434580, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='surgicalproceduraldetail',
            name='docking_ends',
            field=models.TimeField(default=datetime.datetime(2022, 11, 22, 20, 24, 11, 434580, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='surgicalproceduraldetail',
            name='surg_end_time',
            field=models.TimeField(default=datetime.datetime(2022, 11, 22, 20, 24, 11, 434580, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='surgicalproceduraldetail',
            name='surg_start_time',
            field=models.TimeField(default=datetime.datetime(2022, 11, 22, 20, 24, 11, 434580, tzinfo=datetime.timezone.utc)),
        ),
    ]
