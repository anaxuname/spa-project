# Generated by Django 5.0.3 on 2024-03-16 20:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, max_length=100, null=True, verbose_name='Place')),
                ('time_for_habit', models.TimeField(verbose_name='Habit time')),
                ('action', models.CharField(max_length=100, verbose_name='Action')),
                ('is_enjoyable', models.BooleanField(default=False, verbose_name='Is enjoyable')),
                ('periodicity', models.IntegerField(default=1, verbose_name='Periodicity')),
                ('reward', models.CharField(blank=True, max_length=100, null=True, verbose_name='Reward for action')),
                ('continuance', models.IntegerField(verbose_name='Continuance habit in seconds')),
                ('is_public', models.BooleanField(default=False, verbose_name='Is public')),
                ('associated_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.habit', verbose_name='Associated habit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Habit',
                'verbose_name_plural': 'Habits',
            },
        ),
    ]
