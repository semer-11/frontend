# Generated by Django 4.1 on 2023-02-09 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0015_rename_death_date_resident_death_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='kebele_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entry.kebele'),
        ),
    ]
