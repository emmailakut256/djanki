# Generated by Django 4.1.7 on 2023-05-10 10:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("intro", "0002_intros_joined_date_intros_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="intros",
            name="slug",
            field=models.SlugField(default=""),
        ),
    ]
