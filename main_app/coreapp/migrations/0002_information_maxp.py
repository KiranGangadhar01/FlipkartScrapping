# Generated by Django 2.2.5 on 2019-09-28 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='maxP',
            field=models.IntegerField(default=1),
        ),
    ]