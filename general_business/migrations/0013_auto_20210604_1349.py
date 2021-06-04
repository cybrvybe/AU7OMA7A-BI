# Generated by Django 3.2.3 on 2021-06-04 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general_business', '0012_role_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='subtitle',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Short Description'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Business Name'),
        ),
        migrations.AlterField(
            model_name='role',
            name='parent_organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='general_business.organization'),
        ),
        migrations.AlterField(
            model_name='role',
            name='subtitle',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Short Description'),
        ),
        migrations.AlterField(
            model_name='role',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Role Title'),
        ),
        migrations.AlterField(
            model_name='venture',
            name='subtitle',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Short Description'),
        ),
        migrations.AlterField(
            model_name='venture',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Venture Title'),
        ),
    ]