# Generated by Django 5.0.3 on 2024-03-24 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_alter_habit_periodicity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='continuance',
            field=models.PositiveIntegerField(verbose_name='Continuance habit in seconds'),
        ),
    ]
