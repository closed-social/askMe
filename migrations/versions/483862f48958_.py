"""empty message

Revision ID: 483862f48958
Revises: 
Create Date: 2020-08-19 09:56:23.732485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '483862f48958'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('root', sa.BigInteger(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'root')
    # ### end Alembic commands ###
