# Generated by Django 4.0.4 on 2022-05-06 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pixel_app', '0025_comment_thread'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pixel',
            name='color',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, related_name='color', to='pixel_app.color'),
        ),
    ]
