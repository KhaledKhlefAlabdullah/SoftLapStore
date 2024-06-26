# Generated by Django 5.0.6 on 2024-06-26 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("clusters", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customersimilarity",
            name="user1_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user1",
                to="users.user",
            ),
        ),
        migrations.AddField(
            model_name="customersimilarity",
            name="user2_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user2",
                to="users.user",
            ),
        ),
    ]
