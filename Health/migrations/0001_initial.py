# Generated by Django 4.2 on 2023-04-26 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100)),
                ('pemail', models.EmailField(max_length=254)),
                ('pdate', models.DateField(max_length=50)),
                ('pdept', models.CharField(choices=[('General Health', 'General Health'), ('Cardiology', 'Cardiology'), ('Dental', 'Dental'), ('Medical Reasearch', 'Medical Reasearch')], default='Select', max_length=20)),
                ('pcontact', models.CharField(max_length=15)),
                ('pmsg', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Patientinfo',
            },
        ),
    ]