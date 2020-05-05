"""Add user attractions

Revision ID: 0d3affe3e0c1
Revises: 2be373058338
Create Date: 2020-05-05 01:43:24.261296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d3affe3e0c1'
down_revision = '2be373058338'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_attractions',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('attraction_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['attraction_id'], ['attractions.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'attraction_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_attractions')
    # ### end Alembic commands ###