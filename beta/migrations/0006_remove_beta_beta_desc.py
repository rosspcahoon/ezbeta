# Generated by Django 2.0.5 on 2018-05-31 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beta', '0005_auto_20180531_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beta',
            name='beta_desc',
        ),
    ]