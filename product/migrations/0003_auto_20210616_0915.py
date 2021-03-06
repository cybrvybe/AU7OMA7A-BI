# Generated by Django 3.2.3 on 2021-06-16 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general_business', '0001_initial'),
        ('product', '0002_productpriceobj'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceObj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='default title', max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('is_recurring', models.BooleanField(verbose_name='Is the price a recurring amount?')),
                ('reccurence_freq', models.CharField(blank=True, choices=[('daily', 'daily'), ('weekly', 'weekly'), ('monthly', 'monthly'), ('annually', 'annually')], max_length=500, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='product',
            old_name='uploaded_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='uploaded_at',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='service',
            name='is_recurring',
        ),
        migrations.AlterField(
            model_name='product',
            name='parent_organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='general_business.organization'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subtitle',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(blank=True, default='default title', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='parent_organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='general_business.organization'),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(blank=True, default='default title', max_length=500, null=True),
        ),
        migrations.DeleteModel(
            name='ProductPriceObj',
        ),
    ]
