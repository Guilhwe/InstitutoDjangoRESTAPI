# Generated by Django 5.0.3 on 2024-08-27 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instituto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='fecha_nacimiento',
            field=models.DateField(default='2024-08-27'),
            preserve_default=False,
        ),
    ]
