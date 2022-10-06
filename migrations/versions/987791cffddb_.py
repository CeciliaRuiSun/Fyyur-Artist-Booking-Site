"""empty message

Revision ID: 987791cffddb
Revises: d9f5bb186a41
Create Date: 2022-10-06 07:59:14.977352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '987791cffddb'
down_revision = 'd9f5bb186a41'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('website', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artist', 'website')
    # ### end Alembic commands ###
