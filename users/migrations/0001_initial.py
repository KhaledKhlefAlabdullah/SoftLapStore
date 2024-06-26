# Generated by Django 5.0.6 on 2024-06-26 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("clusters", "0001_initial"),
        ("countries", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=255)),
                ("profile", models.TextField(blank=True, null=True)),
                (
                    "user_type",
                    models.CharField(
                        choices=[("admin", "Admin"), ("customer", "Customer")],
                        max_length=20,
                    ),
                ),
                (
                    "cluster_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="clusters.cluster",
                    ),
                ),
                (
                    "country_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="countries.country",
                    ),
                ),
            ],
        ),
    ]
