# Generated by Django 3.2.16 on 2023-01-19 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=20)),
                ('ename', models.CharField(max_length=50)),
                ('eemail', models.EmailField(max_length=254)),
                ('econtact', models.CharField(max_length=50)),
            ],
        ),
    ]
