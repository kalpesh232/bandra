# Generated by Django 4.2.5 on 2023-10-23 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_userregister_imagename_userregister_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregister',
            name='ImageName',
            field=models.CharField(default='0000000', max_length=25),
        ),
        migrations.AlterField(
            model_name='userregister',
            name='pic',
            field=models.ImageField(upload_to='img/'),
        ),
    ]
