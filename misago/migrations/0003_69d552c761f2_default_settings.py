"""default_settings

Revision ID: 69d552c761f2
Revises: ad2a1d098a41
Create Date: 2019-11-17 01:49:55.824480

"""
from datetime import timedelta

from alembic import op
from sqlalchemy import JSON, String
from sqlalchemy.sql import table, column

from misago.utils.strings import get_random_string


# revision identifiers, used by Alembic.
revision = "69d552c761f2"
down_revision = "ad2a1d098a41"
branch_labels = None
depends_on = None

# default data
table = table("misago_settings", column("name", String), column("value", JSON),)

settings = [
    {"name": "forum_name", "value": "Misago"},
    {"name": "jwt_exp", "value": int(timedelta(days=90).total_seconds())},
    {"name": "jwt_secret", "value": get_random_string(64)},
    {"name": "password_min_length", "value": 8},
    {"name": "post_body_min_length", "value": 3},
    {"name": "thread_title_min_length", "value": 5},
    {"name": "thread_title_max_length", "value": 90},
    {"name": "username_min_length", "value": 3},
    {"name": "username_max_length", "value": 10},
]


def upgrade():
    op.bulk_insert(table, settings)


def downgrade():
    pass