# Generated by Django 3.1b1 on 2020-11-30 11:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='full_address',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='website',
            field=models.CharField(default='text', max_length=100),
            preserve_default=False,
        ),
    ]
