# Generated by Django 3.0.6 on 2020-06-02 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_summernote', '0002_update-help_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
