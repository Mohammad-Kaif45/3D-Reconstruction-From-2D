# Generated by Django 5.1.7 on 2025-03-28 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_alter_imageupload_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageupload',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
