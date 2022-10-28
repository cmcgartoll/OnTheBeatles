# Generated by Django 4.1.2 on 2022-10-28 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spotify_id', models.CharField(db_index=True, default='aaaaaaaaaaaaaaaaaaaaa', max_length=22, unique=True)),
                ('name', models.CharField(max_length=140)),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spotify_id', models.CharField(db_index=True, default='aaaaaaaaaaaaaaaaaaaaa', max_length=22, unique=True)),
                ('title', models.CharField(max_length=140)),
                ('release_date', models.DateField()),
                ('cover', models.URLField()),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
                ('artist', models.ManyToManyField(to='spotify.artist')),
            ],
        ),
    ]
