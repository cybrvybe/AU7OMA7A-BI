# Generated by Django 3.2.3 on 2021-06-25 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_feature_subfeatures'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='status',
            field=models.CharField(blank=True, choices=[('Inactive', 'Inactive'), ('In Progress', 'In Progress'), ('Active', 'Active')], max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('Cold', 'Cold'), ('In Queue', 'In Queue'), ('In Progress', 'In Progress'), ('Complete', 'Complete')], max_length=500, null=True),
        ),
    ]
