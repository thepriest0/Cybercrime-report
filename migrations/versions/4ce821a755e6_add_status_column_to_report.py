"""Add status column to Report

Revision ID: 4ce821a755e6
Revises: 7deafd387180
Create Date: 2024-06-21 07:51:42.610147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ce821a755e6'
down_revision = '7deafd387180'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('report', sa.Column('status', sa.String(length=50), nullable=False, server_default='Pending'))
    # Remove server_default after setting the column
    with op.batch_alter_table('report') as batch_op:
        batch_op.alter_column('status', server_default=None)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('report', 'status')
    # ### end Alembic commands ###
