"""empty message

Revision ID: 25cb980c6f1b
Revises: None
Create Date: 2014-08-27 14:11:43.180528

"""

# revision identifiers, used by Alembic.
revision = '25cb980c6f1b'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('owners',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title_number', sa.String(length=10), nullable=True),
    sa.Column('lrid', sa.String(), nullable=True),
    sa.Column('owner_index', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('owners')
    ### end Alembic commands ###