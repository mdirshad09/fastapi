"""create posts table

Revision ID: 6513c52d6f69
Revises: 
Create Date: 2022-08-28 20:24:34.746643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6513c52d6f69'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable = False, primary_key = True)
    , sa.Column('title', sa.String(), nullable = False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
