# Generated by Django 4.1.3 on 2022-11-17 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0008_preprocedurecard_delete_prepocedurecard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preprocedurecard',
            name='id',
        ),
        migrations.AddField(
            model_name='preprocedurecard',
            name='card_id',
            field=models.AutoField(default=-1, primary_key=True, serialize=False),
        ),
    ]