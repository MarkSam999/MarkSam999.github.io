# Generated by Django 5.0.6 on 2025-04-18 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('rating', models.IntegerField()),
                ('message', models.TextField(max_length=500)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name='feedback',
            constraint=models.CheckConstraint(check=models.Q(('rating__lte', 6)), name='less_than_6'),
        ),
        migrations.AddConstraint(
            model_name='feedback',
            constraint=models.CheckConstraint(check=models.Q(('rating__gte', 0)), name='more_than_0'),
        ),
    ]
