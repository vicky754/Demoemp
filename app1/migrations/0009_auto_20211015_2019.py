# Generated by Django 3.1.6 on 2021-10-15 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20211015_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_image',
            field=models.ImageField(blank=True, default='', upload_to='app1/static/app1/images'),
        ),
    ]