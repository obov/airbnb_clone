# Generated by Django 4.1.5 on 2023-01-26 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0002_alter_category_options"),
        ("experiences", "0003_experience_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="experience",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="categories",
                to="categories.category",
            ),
        ),
        migrations.AlterField(
            model_name="experience",
            name="perks",
            field=models.ManyToManyField(
                related_name="categories", to="experiences.perk"
            ),
        ),
    ]