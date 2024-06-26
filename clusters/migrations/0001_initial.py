# Generated by Django 5.0.6 on 2024-06-26 11:59

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cluster",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="CustomerSimilarity",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("similarity", models.FloatField()),
            ],
        ),
    ]
