# Generated by Django 4.2.1 on 2023-06-02 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_person_joined_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]