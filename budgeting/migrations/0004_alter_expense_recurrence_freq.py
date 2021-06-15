# Generated by Django 3.2.3 on 2021-06-11 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgeting', '0003_incomeevent_is_prospective'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='recurrence_freq',
            field=models.CharField(blank=True, choices=[('daily', 'daily'), ('monthly', 'monthly'), ('quarterly', 'quarterly'), ('biannually', 'biannually'), ('annually', 'annually')], max_length=300, null=True, verbose_name='What is the recurrence frequency of this payment? (x weeks, x months, x years)'),
        ),
    ]
