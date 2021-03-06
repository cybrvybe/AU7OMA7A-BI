# Generated by Django 3.2.3 on 2021-06-08 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('general_business', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractFinEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='default title', max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('amount', models.FloatField(blank=True, default=0, null=True, verbose_name='Amount ($)')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AbstractBudgetItem',
            fields=[
                ('abstractfinevent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='budgeting.abstractfinevent')),
                ('is_prospective', models.BooleanField(default=True)),
                ('live_datetime', models.DateTimeField()),
                ('subtitle', models.CharField(blank=True, max_length=300, null=True, verbose_name='Short Description')),
            ],
            options={
                'abstract': False,
            },
            bases=('budgeting.abstractfinevent',),
        ),
        migrations.CreateModel(
            name='IncomeStream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True, verbose_name='Income Source Title')),
                ('parent_organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='general_business.organization')),
                ('parent_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('parent_role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='general_business.role')),
                ('parent_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.service')),
            ],
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='default title', max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('parent_organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='general_business.organization')),
                ('parent_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('parent_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.service')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('abstractbudgetitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='budgeting.abstractbudgetitem')),
                ('is_recurring', models.BooleanField(verbose_name='Is this payment recurring?')),
                ('recurrence_freq', models.CharField(blank=True, max_length=300, null=True, verbose_name='What is the recurrence frequency of this payment? (x weeks, x months, x years)')),
                ('is_business_expense', models.BooleanField(verbose_name='Is this a business expense?')),
                ('is_asset', models.BooleanField(verbose_name='Is this an asset?')),
                ('is_essential', models.BooleanField(blank=True, null=True, verbose_name='Is this expense essential?')),
            ],
            options={
                'abstract': False,
            },
            bases=('budgeting.abstractbudgetitem',),
        ),
        migrations.CreateModel(
            name='IncomeEvent',
            fields=[
                ('abstractfinevent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='budgeting.abstractfinevent')),
                ('uploaded_at', models.DateTimeField(auto_now=True)),
                ('is_recurring', models.BooleanField(verbose_name='Is this income event recurring?')),
                ('recurrence_freq', models.CharField(blank=True, max_length=300, null=True, verbose_name='What is the recurrence frequency of this income event in x weeks, months, or years?')),
                ('parent_income_stream', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='budgeting.incomestream')),
            ],
            options={
                'abstract': False,
            },
            bases=('budgeting.abstractfinevent',),
        ),
        migrations.AddField(
            model_name='abstractbudgetitem',
            name='parent_budget',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budgeting.budget'),
        ),
    ]
