# Generated by Django 4.2.6 on 2023-10-25 03:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tvapp', '0002_puntos'),
    ]

    operations = [
        migrations.CreateModel(
            name='PuntosUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntos', models.IntegerField(default=0)),
                ('ultima_adicion_puntos', models.DateTimeField(null=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Puntos',
        ),
    ]
