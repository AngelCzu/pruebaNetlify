# Generated by Django 4.2.1 on 2023-11-23 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvapp', '0008_mensajechat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(max_length=22)),
            ],
        ),
    ]