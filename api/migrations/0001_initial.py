# Generated by Django 4.2.7 on 2023-11-26 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Api',
            fields=[
                ('API', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Description', models.CharField(max_length=50)),
                ('Auth', models.PositiveSmallIntegerField()),
                ('HTTPS', models.BooleanField(default=False)),
                ('Cors', models.BooleanField(default=False)),
                ('Link', models.URLField()),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categoria')),
            ],
        ),
    ]
