# Generated by Django 3.2.7 on 2021-10-04 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('top', '0004_problem_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='submissionDesc',
        ),
    ]
