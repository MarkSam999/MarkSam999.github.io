# Generated by Django 5.2 on 2025-05-04 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('edu_level', models.CharField(choices=[('9-12', 'Some high school'), ('12+', 'College'), ('12++', 'University')])),
                ('edu_mode', models.CharField(choices=[('<->', 'Regular'), ('--->', 'Long-term'), ('*', 'Online')])),
                ('fav_course', models.CharField(choices=[('math', 'Mathematics'), ('phys', 'Physics'), ('csit', 'Computer Science'), ('eng', 'Literature')])),
            ],
        ),
    ]
