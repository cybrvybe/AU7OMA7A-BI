# Generated by Django 3.2.3 on 2021-06-03 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_delete_feature'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='parent_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Parent Product'),
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Feature Title')),
                ('subtitle', models.CharField(blank=True, max_length=500, null=True, verbose_name='Short Description')),
                ('description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Description')),
                ('parent_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('parent_project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.project')),
                ('parent_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.service')),
            ],
        ),
    ]
