# Generated by Django 2.2.1 on 2019-06-16 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SocialAuthProvider",
            fields=[
                (
                    "provider",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                (
                    "button_text",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("button_color", models.CharField(blank=True, max_length=7, null=True)),
                (
                    "settings",
                    models.JSONField(default=dict),
                ),
                ("is_active", models.BooleanField(default=False)),
                ("order", models.IntegerField(default=0)),
            ],
            options={"ordering": ["order"]},
        )
    ]
