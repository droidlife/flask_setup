"""empty message

Revision ID: 7b637d7b775e
Revises: d6396ebe8dc7
Create Date: 2018-09-13 21:17:26.569014

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7b637d7b775e'
down_revision = 'd6396ebe8dc7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('order', 'customer_email',
               existing_type=mysql.VARCHAR(length=120),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('order', 'customer_email',
               existing_type=mysql.VARCHAR(length=120),
               nullable=False)
    # ### end Alembic commands ###