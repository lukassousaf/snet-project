# Generated by Django 3.2.6 on 2021-08-15 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20210814_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='telefone',
            field=models.CharField(max_length=15),
        ),
    ]