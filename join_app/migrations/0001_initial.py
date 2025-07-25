# Generated by Django 5.1.5 on 2025-07-11 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=225)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone", models.CharField(max_length=225)),
                ("initials", models.CharField(blank=True, max_length=5)),
                ("color", models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name="SubTask",
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
                ("title", models.CharField(max_length=225)),
                ("completed", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Task",
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
                ("title", models.CharField(max_length=225)),
                (
                    "board_category",
                    models.CharField(
                        choices=[
                            ("to-do", "To do"),
                            ("in-progress", "In Progress"),
                            ("await-feedback", "Await feedback"),
                            ("done", "Done"),
                        ],
                        max_length=225,
                    ),
                ),
                ("description", models.CharField(max_length=225)),
                ("date", models.CharField(max_length=225)),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("urgent", "Urgent"),
                            ("medium", "Medium"),
                            ("low", "Low"),
                        ],
                        max_length=225,
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("technical task", "Technical Task"),
                            ("user story", "User Story"),
                        ],
                        max_length=225,
                    ),
                ),
            ],
        ),
    ]
