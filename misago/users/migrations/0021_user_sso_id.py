# Generated by Django 2.2.3 on 2019-08-15 16:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("misago_users", "0020_set_dj_partial_indexes")]

    operations = [
        migrations.AddField(
            model_name="user",
            name="sso_id",
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        )
    ]
