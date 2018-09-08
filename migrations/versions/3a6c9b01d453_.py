"""empty message

Revision ID: 3a6c9b01d453
Revises: 943b943147f3
Create Date: 2018-09-08 17:35:08.365255

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3a6c9b01d453'
down_revision = '943b943147f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('order', 'customer_name',
               existing_type=mysql.VARCHAR(length=80),
               type_=sa.String(length=100),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('order', 'customer_name',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=80),
               existing_nullable=False)
    # ### end Alembic commands ###
