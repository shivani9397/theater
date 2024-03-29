# Generated by Django 2.2.6 on 2019-11-21 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mname', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aid', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('Mov_actor', models.ManyToManyField(to='movies.Movies')),
            ],
        ),
    ]
