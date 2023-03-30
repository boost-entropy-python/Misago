# Generated by Django 1.11.9 on 2018-03-18 20:40
from django.db import migrations

_ = lambda s: s


def create_default_categories_roles(apps, schema_editor):
    CategoryRole = apps.get_model("misago_categories", "CategoryRole")

    CategoryRole.objects.create(
        name=_("Q&A user"),
        permissions={
            # best answers perms
            "misago.threads.permissions.bestanswers": {
                "can_mark_best_answers": 1,
                "can_change_marked_answers": 1,
                "best_answer_change_time": 60 * 36,  # 1.5 day
            }
        },
    )

    CategoryRole.objects.create(
        name=_("Q&A moderator"),
        permissions={
            # best answers perms
            "misago.threads.permissions.bestanswers": {
                "can_mark_best_answers": 2,
                "can_change_marked_answers": 2,
                "best_answer_change_time": 0,
            }
        },
    )


class Migration(migrations.Migration):
    dependencies = [("misago_categories", "0006_moderation_queue_roles")]

    operations = [migrations.RunPython(create_default_categories_roles)]
