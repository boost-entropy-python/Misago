# Generated by Django 1.11.5 on 2017-10-15 20:10
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("misago_readtracker", "0003_migrate_reads_to_posts")]

    operations = [
        migrations.RemoveField(model_name="categoryread", name="category"),
        migrations.RemoveField(model_name="categoryread", name="user"),
        migrations.RemoveField(model_name="threadread", name="category"),
        migrations.RemoveField(model_name="threadread", name="thread"),
        migrations.RemoveField(model_name="threadread", name="user"),
        migrations.DeleteModel(name="CategoryRead"),
        migrations.DeleteModel(name="ThreadRead"),
    ]
