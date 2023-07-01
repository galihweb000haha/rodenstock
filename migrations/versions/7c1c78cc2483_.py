"""empty message

Revision ID: 7c1c78cc2483
Revises: a0462e2f9822
Create Date: 2023-06-05 19:57:09.457121

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7c1c78cc2483'
down_revision = 'a0462e2f9822'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('admin_prodi', schema=None) as batch_op:
        batch_op.add_column(sa.Column('prodi_id', sa.Integer(), nullable=False))
        batch_op.alter_column('id',
               existing_type=mysql.INTEGER(),
               nullable=False)
        batch_op.create_foreign_key(None, 'prodi', ['prodi_id'], ['id'])

    with op.batch_alter_table('mahasiswa', schema=None) as batch_op:
        batch_op.alter_column('gender',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mahasiswa', schema=None) as batch_op:
        batch_op.alter_column('gender',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)

    with op.batch_alter_table('admin_prodi', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('id',
               existing_type=mysql.INTEGER(),
               nullable=True)
        batch_op.drop_column('prodi_id')

    # ### end Alembic commands ###