# Generated by Django 3.2.3 on 2021-06-21 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0001_initial'),
        ('metrics', '0001_initial'),
        ('content', '0002_abstractdescmodel_book_chapter_chapterintroquote_chaptersection_paragraph'),
        ('analytics', '0002_auto_20210615_1617'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AutonomousAnalysis',
            new_name='Bot',
        ),
    ]
