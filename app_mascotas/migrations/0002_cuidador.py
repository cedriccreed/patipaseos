# Generated by Django 4.2.9 on 2024-01-10 23:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_mascotas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuidador',
            fields=[
                ('id_cuidador', models.AutoField(primary_key=True, serialize=False)),
                ('especializacion', models.CharField(max_length=50)),
                ('propietario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
