# Generated by Django 4.2.1 on 2023-06-20 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissionresult',
            name='ranking',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='admissionresult',
            name='studentId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='schoolName',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='stdName',
            field=models.CharField(max_length=100),
        ),
    ]
