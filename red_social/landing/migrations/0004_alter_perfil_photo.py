# Generated by Django 5.1.6 on 2025-05-23 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_perfil_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='img/pfp/'),
        ),
    ]
