# Generated by Django 4.2.5 on 2023-10-10 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=10)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
    ]
