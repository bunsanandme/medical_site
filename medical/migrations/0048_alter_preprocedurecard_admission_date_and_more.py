# Generated by Django 4.1.3 on 2022-11-23 18:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0047_alter_preprocedurecard_admission_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preprocedurecard',
            name='admission_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 18, 59, 45, 687184, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='preprocedurecard',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 18, 59, 45, 687184, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='preprocedurecard',
            name='sign_date',
            field=models.DateField(default=datetime.datetime(2022, 11, 23, 18, 59, 45, 687184, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='surgicalproceduraldetail',
            name='console_end_time',
            field=models.TimeField(default=datetime.datetime(2022, 11, 23, 18, 59, 45, 690174, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='surgicalproceduraldetail',
            name='console_start_time',
            field=models.TimeField(default=datetime.datetime(2022, 11, 23, 18, 59, 45, 690174, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='surgicalproceduraldetail',
            name='docking_begins',
            field=models.TimeField(default=datetime.datetime(2022, 11, 23, 18, 59, 45, 690174, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='surgicalproceduraldetail',
            name='docking_ends',
            field=models.TimeField(default=datetime.datetime(2022, 11, 23, 18, 59, 45, 690174, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='surgicalproceduraldetail',
            name='surg_end_time',
            field=models.TimeField(default=datetime.datetime(2022, 11, 23, 18, 59, 45, 690174, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='surgicalproceduraldetail',
            name='surg_start_time',
            field=models.TimeField(default=datetime.datetime(2022, 11, 23, 18, 59, 45, 690174, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='InstrumentUsed',
            fields=[
                ('inst_use_id', models.AutoField(primary_key=True, serialize=False)),
                ('diameter', models.CharField(blank=True, choices=[('5mm', '5mm'), ('10mm', '10mm')], default=' ', max_length=4)),
                ('dimension', models.CharField(blank=True, choices=[('2D', '2D'), ('3D', '3D'), ('4D', '4D')], default=' ', max_length=2)),
                ('optic_degree', models.CharField(blank=True, choices=[('0°', '0°'), ('30°', '30°')], default=' ', max_length=10)),
                ('manufacturer', models.CharField(blank=True, choices=[('Conmed', 'Conmed'), ('NovaDAQ', 'NovaDAQ'), ('Wolf', 'Wolf'), ('Stryker', 'Stryker'), ('Storz', 'Storz'), ('Olympus', 'Olympus')], default=' ', max_length=10)),
                ('table_pi1_3', models.BooleanField(blank=True, default=False, null=True)),
                ('table_pi2_3', models.BooleanField(blank=True, default=False, null=True)),
                ('table_pi3_3', models.BooleanField(blank=True, default=False, null=True)),
                ('table_pi4_3', models.BooleanField(blank=True, default=False, null=True)),
                ('table_mi1_3', models.BooleanField(blank=True, default=False, null=True)),
                ('table_mi2_3', models.BooleanField(blank=True, default=False, null=True)),
                ('table_mi3_3', models.BooleanField(blank=True, default=False, null=True)),
                ('table_bi1_3', models.BooleanField(blank=True, default=False, null=True)),
                ('table_bi2_3', models.BooleanField(blank=True, default=False, null=True)),
                ('table_pi1_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_pi2_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_pi3_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_pi4_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_pi5_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_pi6_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_pi7_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_pi8_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_pi9_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_pi10_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_pi11_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_pi12_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_pi13_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_pi14_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_pi15_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_pi16_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_pi17_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_mi1_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_mi2_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_mi3_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_mi4_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_mi5_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_mi6_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_mi7_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_mi8_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_bi1_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_bi2_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_bi3_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_bi4_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_bi5_5', models.BooleanField(blank=True, default=False, null=True)),
                ('table_pi1_10', models.BooleanField(blank=True, default=False, null=True)),
                ('table_pi2_10', models.BooleanField(blank=True, default=False, null=True)),
                ('table_ca1', models.BooleanField(blank=True, default=False, null=True)),
                ('table_us', models.BooleanField(blank=True, default=False, null=True)),
                ('table_ai1', models.BooleanField(blank=True, default=False, null=True)),
                ('table_ai2', models.BooleanField(blank=True, default=False, null=True)),
                ('table_ai3', models.BooleanField(blank=True, default=False, null=True)),
                ('table_ai4', models.BooleanField(blank=True, default=False, null=True)),
                ('table_rad1', models.BooleanField(blank=True, default=False, null=True)),
                ('table_rad2', models.BooleanField(blank=True, default=False, null=True)),
                ('table_rad3', models.BooleanField(blank=True, default=False, null=True)),
                ('card_id', models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='medical.card')),
            ],
        ),
    ]
