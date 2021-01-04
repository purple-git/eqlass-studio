# Generated by Django 3.1b1 on 2020-11-27 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='pics')),
                ('title', models.CharField(max_length=100)),
                ('overview', models.CharField(max_length=200)),
            ],
        ),
    ]