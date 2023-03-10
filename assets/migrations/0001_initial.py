# Generated by Django 4.1.5 on 2023-01-25 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("rooms", "0005_room_category"),
        ("experiences", "0003_experience_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                ("details", models.CharField(blank=True, default="", max_length=250)),
                ("description", models.TextField(blank=True, default="")),
                ("file", models.FileField(upload_to="")),
                (
                    "experience",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="experiences.experience",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Photo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                ("details", models.CharField(blank=True, default="", max_length=250)),
                ("description", models.TextField(blank=True, default="")),
                ("file", models.ImageField(upload_to="")),
                (
                    "experience",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="experiences.experience",
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rooms.room",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
