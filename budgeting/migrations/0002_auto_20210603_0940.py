# Generated by Django 3.2.3 on 2021-06-03 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general_business', '0009_auto_20210602_1631'),
        ('budgeting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='parent_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='general_business.product'),
        ),
        migrations.AddField(
            model_name='budget',
            name='parent_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='general_business.service'),
        ),
        migrations.AlterField(
            model_name='budget',
            name='parent_organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='general_business.organization'),
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Expense Title')),
                ('subtitle', models.CharField(blank=True, max_length=300, null=True, verbose_name='Short Description')),
                ('cost', models.FloatField(blank=True, null=True, verbose_name='Cost ($)')),
                ('is_recurring', models.BooleanField(verbose_name='Is this payment recurring?')),
                ('recurrence_freq', models.CharField(blank=True, max_length=300, null=True, verbose_name='What is the recurrence frequency of this payment? (x weeks, x months, x years)')),
                ('is_prospective', models.BooleanField(verbose_name='Is this payment prospective?')),
                ('is_business_expense', models.BooleanField(verbose_name='Is this a business expense?')),
                ('is_asset', models.BooleanField(verbose_name='Is this an asset?')),
                ('parent_budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budgeting.budget')),
            ],
        ),
    ]