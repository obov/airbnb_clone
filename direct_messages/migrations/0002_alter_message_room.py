# Generated by Django 4.1.5 on 2023-01-25 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("direct_messages", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="direct_messages.chatroom",
            ),
        ),
    ]
