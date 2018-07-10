# Generated by Django 2.0.7 on 2018-07-10 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_inventory_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pir',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
