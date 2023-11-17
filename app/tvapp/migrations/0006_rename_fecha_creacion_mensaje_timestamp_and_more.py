# Generated by Django 4.2.6 on 2023-11-14 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvapp', '0005_mensaje'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensaje',
            old_name='fecha_creacion',
            new_name='timestamp',
        ),
        migrations.AddField(
            model_name='mensaje',
            name='destacado',
            field=models.BooleanField(default=False),
        ),
    ]