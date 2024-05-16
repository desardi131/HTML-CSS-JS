# Generated by Django 5.0.6 on 2024-05-16 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('apellidos', models.CharField(max_length=64)),
                ('rfc', models.CharField(max_length=15, unique=True)),
                ('fecha_nacimiento', models.DateField()),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
    ]
