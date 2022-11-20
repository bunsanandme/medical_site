# Generated by Django 4.1.3 on 2022-11-20 12:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0017_rename_pacient_id_medicalhistory_card_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalhistory',
            name='card_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medical.card'),
        ),
        migrations.AlterField(
            model_name='preprocedurecard',
            name='admission_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 20, 12, 6, 11, 675713, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='preprocedurecard',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 20, 12, 6, 11, 675713, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='preprocedurecard',
            name='sign_date',
            field=models.DateField(default=datetime.datetime(2022, 11, 20, 12, 6, 11, 675713, tzinfo=datetime.timezone.utc)),
        ),
    ]
