# Generated by Django 5.0.4 on 2024-04-17 21:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0002_alter_article_options_scope_tag_scope_tag"),
    ]

    operations = [
        migrations.AddField(
            model_name="scope",
            name="is_main",
            field=models.BooleanField(default=0, verbose_name="Основное"),
        ),
    ]
