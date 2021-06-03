# Generated by Django 3.2.3 on 2021-06-03 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general_business', '0009_auto_20210602_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Budget Title')),
                ('parent_organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general_business.organization')),
            ],
        ),
    ]
