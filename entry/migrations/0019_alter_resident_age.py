# Generated by Django 4.1 on 2023-02-09 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0018_rename_kebele_name_resident_kebele_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]