# Generated by Django 1.11.1 on 2017-05-21 17:52
import django.contrib.postgres.indexes
from django.contrib.postgres.operations import BtreeGinExtension
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("misago_threads", "0004_update_settings")]

    operations = [
        BtreeGinExtension(),
        migrations.AddIndex(
            model_name="post",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["search_vector"], name="misago_thre_search__b472a2_gin"
            ),
        ),
    ]
