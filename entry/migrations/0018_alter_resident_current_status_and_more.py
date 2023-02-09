# Generated by Django 4.1 on 2023-02-09 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0017_alter_resident_options_alter_resident_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='current_status',
            field=models.CharField(blank=True, choices=[('alive', 'alive'), ('dead', 'dead')], default='alive', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='resident',
            name='marital_status',
            field=models.CharField(choices=[('single', 'single'), ('married', 'married'), ('divorced', 'divorced')], default='single', max_length=200),
        ),
    ]
