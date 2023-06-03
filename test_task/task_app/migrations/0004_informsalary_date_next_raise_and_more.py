# Generated by Django 4.2.1 on 2023-06-02 09:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task_app', '0003_alter_informsalary_summ_check'),
    ]

    operations = [
        migrations.AddField(
            model_name='informsalary',
            name='date_next_raise',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='informsalary',
            name='date_check',
            field=models.DateField(default=datetime.date(2023, 6, 2)),
        ),
        migrations.CreateModel(
            name='CodeConfirmEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_verify', models.CharField(max_length=1000)),
                ('email_for_verify', models.CharField(max_length=1000)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
