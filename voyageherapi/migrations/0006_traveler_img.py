# Generated by Django 4.2.2 on 2023-06-22 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voyageherapi', '0005_alter_guide_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='traveler',
            name='img',
            field=models.URLField(default=None, null=True),
        ),
    ]
