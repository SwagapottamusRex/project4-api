# Generated by Django 4.0.4 on 2022-04-22 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pixel_app', '0023_remove_thread_reply_thread_thread_reply_thread'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='reply_thread',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='pixel_app.comment'),
        ),
    ]
