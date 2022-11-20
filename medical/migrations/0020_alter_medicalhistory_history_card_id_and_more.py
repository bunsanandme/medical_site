# Generated by Django 4.1.3 on 2022-11-20 12:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0019_alter_preprocedurecard_admission_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalhistory',
            name='history_card_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='preprocedurecard',
            name='admission_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 20, 12, 24, 15, 927195, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='preprocedurecard',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 20, 12, 24, 15, 927195, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='preprocedurecard',
            name='sign_date',
            field=models.DateField(default=datetime.datetime(2022, 11, 20, 12, 24, 15, 927195, tzinfo=datetime.timezone.utc)),
        ),
    ]