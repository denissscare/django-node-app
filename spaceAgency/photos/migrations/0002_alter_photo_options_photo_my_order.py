# Generated by Django 4.2.16 on 2024-11-10 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['my_order']},
        ),
        migrations.AddField(
            model_name='photo',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
