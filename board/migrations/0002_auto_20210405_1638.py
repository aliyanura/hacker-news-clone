# Generated by Django 3.1.7 on 2021-04-05 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="story",
            options={"ordering": ["-created_at"],
                     "verbose_name_plural": "stories"},
        ),
        migrations.RenameField(
            model_name="story",
            old_name="author",
            new_name="created_by",
        ),
    ]
