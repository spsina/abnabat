# Generated by Django 2.0.7 on 2018-07-10 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package',
            old_name='clinet',
            new_name='client',
        ),
    ]
