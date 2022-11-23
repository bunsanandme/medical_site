# Generated by Django 4.1.3 on 2022-11-23 17:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0046_alter_preprocedurecard_admission_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preprocedurecard',
            name='admission_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 17, 17, 38, 421457, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='preprocedurecard',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 17, 17, 38, 421457, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='preprocedurecard',
            name='sign_date',
            field=models.DateField(default=datetime.datetime(2022, 11, 23, 17, 17, 38, 421457, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='surgicalproceduraldetail',
            name='console_end_time',
            field=models.TimeField(default=datetime.datetime(2022, 11, 23, 17, 17, 38, 425433, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='surgicalproceduraldetail',
            name='console_start_time',
            field=models.TimeField(default=datetime.datetime(2022, 11, 23, 17, 17, 38, 425433, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='surgicalproceduraldetail',
            name='docking_begins',
            field=models.TimeField(default=datetime.datetime(2022, 11, 23, 17, 17, 38, 425433, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='surgicalproceduraldetail',
            name='docking_ends',
            field=models.TimeField(default=datetime.datetime(2022, 11, 23, 17, 17, 38, 425433, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='surgicalproceduraldetail',
            name='surg_end_time',
            field=models.TimeField(default=datetime.datetime(2022, 11, 23, 17, 17, 38, 425433, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='surgicalproceduraldetail',
            name='surg_start_time',
            field=models.TimeField(default=datetime.datetime(2022, 11, 23, 17, 17, 38, 425433, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='RobotMalfunction',
            fields=[
                ('rob_mal_id', models.AutoField(primary_key=True, serialize=False)),
                ('malfunction', models.CharField(blank=True, choices=[('Неисправность консоли', 'Неисправность консоли'), ('Неисправность монитора/камеры', 'Неисправность монитора/камеры'), ('Ограниченное движение', 'Ограниченное движение'), ('Столкновение', 'Столкновение'), ('Другое', 'Другое')], default=' ', max_length=50)),
                ('comment', models.TextField(blank=True, default=' ')),
                ('card_id', models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='medical.card')),
            ],
        ),
    ]
