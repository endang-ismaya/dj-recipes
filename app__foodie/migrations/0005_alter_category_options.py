# Generated by Django 5.0.6 on 2024-05-19 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app__foodie", "0004_delete_recipe"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"ordering": ["name"], "verbose_name_plural": "Categories"},
        ),
    ]