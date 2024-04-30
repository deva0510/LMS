# Generated by Django 5.0.1 on 2024-02-22 10:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0135_teachers_photo_alter_leave_today_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='admissioncont',
            name='content1',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='admissioncont',
            name='heading1',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='admissioncont',
            name='images1',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='today',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 22, 10, 25, 10, 595971)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='half_daytime',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 2, 22, 10, 25, 10, 547789)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='in_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 2, 22, 10, 25, 10, 547789)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='late_mark_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 2, 22, 10, 25, 10, 547789)),
        ),
        migrations.AlterField(
            model_name='teacher_shifts',
            name='out_time',
            field=models.TimeField(verbose_name=datetime.datetime(2024, 2, 22, 10, 25, 10, 547789)),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='dob',
            field=models.DateField(default=datetime.datetime(2024, 2, 22, 10, 25, 10, 547789)),
        ),
    ]
