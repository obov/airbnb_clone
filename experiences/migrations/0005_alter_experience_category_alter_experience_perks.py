# Generated by Django 4.1.5 on 2023-01-26 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0002_alter_category_options"),
        ("experiences", "0004_alter_experience_category_alter_experience_perks"),
    ]

    operations = [
        migrations.AlterField(
            model_name="experience",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="experiences",
                to="categories.category",
            ),
        ),
        migrations.AlterField(
            model_name="experience",
            name="perks",
            field=models.ManyToManyField(
                related_name="experiences", to="experiences.perk"
            ),
        ),
    ]
