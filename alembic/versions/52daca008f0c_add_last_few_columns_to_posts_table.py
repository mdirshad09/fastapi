"""add last few columns to posts table

Revision ID: 52daca008f0c
Revises: 48be59334ded
Create Date: 2022-08-29 20:55:06.655041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52daca008f0c'
down_revision = '48be59334ded'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable = False, server_default= 'TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default= sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
