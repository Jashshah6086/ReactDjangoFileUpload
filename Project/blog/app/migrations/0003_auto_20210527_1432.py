# Generated by Django 3.1.2 on 2021-05-27 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Title', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
