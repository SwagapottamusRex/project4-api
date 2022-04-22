# Generated by Django 4.0.4 on 2022-04-21 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pixel_app', '0019_remove_community_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='community', to=settings.AUTH_USER_MODEL),
        ),
    ]
