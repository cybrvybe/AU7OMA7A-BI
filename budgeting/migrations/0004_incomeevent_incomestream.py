# Generated by Django 3.2.3 on 2021-06-03 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('general_business', '0011_auto_20210603_1328'),
        ('budgeting', '0003_auto_20210603_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncomeStream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='general_business.organization')),
                ('parent_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('parent_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.service')),
            ],
        ),
        migrations.CreateModel(
            name='IncomeEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now=True)),
                ('amount', models.FloatField(verbose_name='Income Amount ($)')),
                ('is_recurring', models.BooleanField(verbose_name='Is this income event recurring?')),
                ('recurrence_freq', models.CharField(max_length=300, verbose_name='What is the recurrence frequency of this income event in x weeks, months, or years?')),
                ('parent_income_stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budgeting.incomestream')),
            ],
        ),
    ]