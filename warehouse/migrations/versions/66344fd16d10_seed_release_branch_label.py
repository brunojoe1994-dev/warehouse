# SPDX-License-Identifier: Apache-2.0
"""
Seed release branch label

Revision ID: 66344fd16d10
Revises: b8e6e0867168
Create Date: 2026-04-21 17:27:29.126731
"""

import sqlalchemy as sa

from alembic import op

revision = "66344fd16d10"
down_revision = "b8e6e0867168"
branch_labels = ("release",)
depends_on = None

# Note: It is VERY important to ensure that a migration does not lock for a
#       long period of time and to ensure that each individual migration does
#       not break compatibility with the *previous* version of the code base.
#       This is because the migrations will be ran automatically as part of the
#       deployment process, but while the previous version of the code is still
#       up and running. Thus backwards incompatible changes must be broken up
#       over multiple migrations inside of multiple pull requests in order to
#       phase them in over multiple deploys.
#
#       By default, migrations cannot wait more than 4s on acquiring a lock
#       and each individual statement cannot take more than 5s. This helps
#       prevent situations where a slow migration takes the entire site down.
#
#       If you need to increase this timeout for a migration, you can do so
#       by adding:
#
#           op.execute("SET statement_timeout = 5000")
#           op.execute("SET lock_timeout = 4000")
#
#       To whatever values are reasonable for this migration as part of your
#       migration.


def upgrade():
    pass


def downgrade():
    pass
