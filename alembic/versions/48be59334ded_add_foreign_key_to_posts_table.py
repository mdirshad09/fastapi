"""add foreign-key to posts table

Revision ID: 48be59334ded
Revises: 228bd6517b96
Create Date: 2022-08-29 19:44:18.269191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48be59334ded'
down_revision = '228bd6517b96'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable= False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users',
                        local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
