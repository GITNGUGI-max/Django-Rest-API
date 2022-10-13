# Generated by Django 3.0.6 on 2020-06-01 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200601_0432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='language',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Author'),
        ),
    ]
