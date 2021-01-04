# Generated by Django 3.1b1 on 2020-12-02 14:29

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20201128_0230'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoticeBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
    ]
