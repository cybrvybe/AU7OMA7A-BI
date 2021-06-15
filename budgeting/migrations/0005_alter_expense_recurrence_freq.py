# Generated by Django 3.2.3 on 2021-06-11 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgeting', '0004_alter_expense_recurrence_freq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='recurrence_freq',
            field=models.CharField(blank=True, choices=[('daily', 'daily'), ('monthly', 'monthly'), ('quarterly', 'quarterly'), ('biannual', 'biannual'), ('annual', 'annual')], max_length=300, null=True, verbose_name='What is the recurrence frequency of this payment? (x weeks, x months, x years)'),
        ),
    ]
