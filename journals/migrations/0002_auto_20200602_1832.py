# Generated by Django 3.0.6 on 2020-06-02 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='Patient',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='Records',
        ),
        migrations.RemoveField(
            model_name='records',
            name='Doctor',
        ),
        migrations.RemoveField(
            model_name='records',
            name='Patient',
        ),
    ]
