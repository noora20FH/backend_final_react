# Generated by Django 4.2.1 on 2023-06-20 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_admissionresult_ranking_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admissionresult',
            old_name='studentId',
            new_name='stId',
        ),
        migrations.RenameField(
            model_name='admissionresult',
            old_name='stdName',
            new_name='student_name',
        ),
    ]
