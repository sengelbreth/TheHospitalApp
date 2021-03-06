# Generated by Django 3.0.6 on 2020-05-30 20:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('LastName', models.CharField(max_length=200)),
                ('Field', models.CharField(help_text='field of work for the Doctor', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this patient', primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('LastName', models.CharField(max_length=200)),
                ('Adresse', models.CharField(max_length=200)),
                ('Doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='journals.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('History', models.CharField(max_length=1000)),
                ('Doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='journals.Doctor')),
                ('Patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='journals.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='Records',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='journals.Records'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='Patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='journals.Patient'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='Records',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='journals.Records'),
        ),
    ]
