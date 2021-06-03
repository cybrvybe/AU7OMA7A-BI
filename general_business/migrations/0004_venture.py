# Generated by Django 3.2.3 on 2021-06-02 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_business', '0003_alter_organization_parent_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Venture Title')),
                ('subtitle', models.CharField(max_length=300, verbose_name='Short Description')),
                ('is_product', models.BooleanField(verbose_name='Does this business venture contain/exist as a product?')),
                ('is_service', models.BooleanField(verbose_name='Does this business venture contain/exist as a service?')),
                ('is_campaign', models.BooleanField(verbose_name='Does this business venture contain/exist as a campaign?')),
            ],
        ),
    ]