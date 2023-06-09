# Generated by Django 4.2.2 on 2023-06-06 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Traveler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=250)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('guide_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voyageherapi.guide')),
                ('traveler_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voyageherapi.traveler')),
            ],
        ),
        migrations.AddField(
            model_name='guide',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guides', to='voyageherapi.location'),
        ),
        migrations.AddField(
            model_name='guide',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='FaveGuide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guide_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribers', to='voyageherapi.guide')),
                ('traveler_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribed', to='voyageherapi.traveler')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=500)),
                ('img_url', models.URLField()),
                ('date_time', models.DateField()),
                ('duration', models.IntegerField()),
                ('available_spots', models.IntegerField()),
                ('attendees', models.ManyToManyField(related_name='attending', to='voyageherapi.traveler')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='voyageherapi.guide')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='voyageherapi.location')),
            ],
        ),
    ]
