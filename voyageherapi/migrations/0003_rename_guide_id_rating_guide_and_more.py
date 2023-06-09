# Generated by Django 4.2.2 on 2023-06-09 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voyageherapi', '0002_alter_event_date_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='guide_id',
            new_name='guide',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='rating',
            new_name='score',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='traveler_id',
            new_name='traveler',
        ),
        migrations.AddField(
            model_name='rating',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
    ]