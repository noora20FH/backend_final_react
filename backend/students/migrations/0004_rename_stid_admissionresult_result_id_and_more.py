# Generated by Django 4.2.1 on 2023-06-20 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_rename_studentid_admissionresult_stid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admissionresult',
            old_name='stId',
            new_name='result_id',
        ),
        migrations.RenameField(
            model_name='admissionresult',
            old_name='result',
            new_name='results',
        ),
        migrations.AlterField(
            model_name='admissionresult',
            name='student_name',
            field=models.CharField(max_length=150),
        ),
    ]
