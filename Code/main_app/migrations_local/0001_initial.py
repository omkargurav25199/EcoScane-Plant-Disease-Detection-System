# Generated by Django 3.2 on 2022-04-17 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='plants/')),
            ],
        ),
        migrations.CreateModel(
            name='Soils',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='soils/')),
                ('plant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.plants')),
            ],
        ),
        migrations.CreateModel(
            name='AreaDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('soil', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.soils')),
            ],
        ),
    ]
