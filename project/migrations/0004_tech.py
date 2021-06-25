# Generated by Django 3.2.3 on 2021-06-25 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='default title', max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('tech_category', models.CharField(blank=True, choices=[('Front-End', 'Front-End'), ('DevOps', 'DevOps'), ('Back-End', 'Back-End'), ('Testing', 'Testing'), ('Database', 'Database'), ('Data Science', 'Data Science')], max_length=500, null=True)),
                ('parent_feature', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project.feature')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
