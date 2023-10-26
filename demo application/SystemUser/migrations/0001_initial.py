# Generated by Django 4.2.5 on 2023-09-23 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('profile', models.CharField(max_length=50)),
                ('reg_number', models.CharField(max_length=50)),
                ('reg_date', models.DateField()),
                ('id_number', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
