# Generated by Django 3.2.3 on 2021-06-03 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('budgeting', '0002_auto_20210603_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='parent_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AlterField(
            model_name='budget',
            name='parent_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.service'),
        ),
    ]