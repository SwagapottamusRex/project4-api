# Generated by Django 4.0.4 on 2022-04-16 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel_app', '0008_alter_color_color_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='color_name',
            field=models.CharField(max_length=30),
        ),
    ]
