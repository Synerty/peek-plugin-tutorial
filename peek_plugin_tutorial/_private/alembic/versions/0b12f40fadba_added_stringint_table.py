"""Added StringInt Table

Peek Plugin Database Migration Script

Revision ID: 0b12f40fadba
Revises: 
Create Date: 2017-03-21 01:29:00.326202

"""

# revision identifiers, used by Alembic.
revision = '0b12f40fadba'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
import geoalchemy2


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('StringIntTuple',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('string1', sa.String(length=50), nullable=True),
    sa.Column('int1', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='pl_tutorial'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('StringIntTuple', schema='pl_tutorial')
    # ### end Alembic commands ###