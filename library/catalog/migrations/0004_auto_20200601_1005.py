# Generated by Django 3.0.6 on 2020-06-01 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20200601_0951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinstance',
            old_name='imprints',
            new_name='imprint',
        ),
    ]