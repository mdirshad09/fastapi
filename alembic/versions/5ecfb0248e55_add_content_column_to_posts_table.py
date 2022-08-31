"""add content column to posts table

Revision ID: 5ecfb0248e55
Revises: 6513c52d6f69
Create Date: 2022-08-28 20:40:29.811131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ecfb0248e55'
down_revision = '6513c52d6f69'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable = False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
