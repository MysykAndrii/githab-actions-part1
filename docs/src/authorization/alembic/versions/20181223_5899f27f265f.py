"""init

Revision ID: 5899f27f265f
Revises: 
Create Date: 2018-12-23 16:39:13.677058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5899f27f265f'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('entries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Unicode(length=255), nullable=False),
    sa.Column('body', sa.UnicodeText(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('edited', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_entries')),
    sa.UniqueConstraint('title', name=op.f('uq_entries_title'))
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(length=255), nullable=False),
    sa.Column('password', sa.Unicode(length=255), nullable=False),
    sa.Column('last_logged', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('name', name=op.f('uq_users_name'))
    )
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('entries')
    # ### end Alembic commands ###
