# Generated by Django 4.2.1 on 2023-06-01 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0002_alter_informsalary_summ_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informsalary',
            name='summ_check',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
    ]
