# Generated by Django 5.1.4 on 2025-01-12 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_rndaresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdetail',
            name='number_of_siblings',
            field=models.IntegerField(null=True),
        ),
    ]
