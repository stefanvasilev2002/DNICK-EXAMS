# Generated by Django 5.0.6 on 2024-09-14 17:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Painter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_and_surname', models.CharField(max_length=100)),
                ('style', models.CharField(choices=[('IMP', 'Impressionism'), ('POP', 'Pop Art'), ('GRA', 'Graffiti')], max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='images/')),
                ('exhibition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.exhibition')),
                ('painter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.painter')),
            ],
        ),
    ]