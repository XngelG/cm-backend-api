# Generated by Django 4.0.1 on 2022-01-10 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
