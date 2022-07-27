# Generated by Django 4.0.2 on 2022-03-08 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LeagueOfLegends', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='friend',
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend', models.CharField(blank=True, max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LeagueOfLegends.user')),
            ],
        ),
    ]
