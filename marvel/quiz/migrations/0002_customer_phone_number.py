# Generated by Django 5.1.5 on 2025-01-28 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="phone_number",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
