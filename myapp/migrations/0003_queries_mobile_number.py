# Generated by Django 3.2.10 on 2022-08-08 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_queries'),
    ]

    operations = [
        migrations.AddField(
            model_name='queries',
            name='mobile_number',
            field=models.IntegerField(blank=True, default=0, max_length=10, verbose_name='zipcode'),
        ),
    ]
