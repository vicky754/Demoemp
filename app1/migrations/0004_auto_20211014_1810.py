# Generated by Django 3.1.6 on 2021-10-14 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20211012_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]