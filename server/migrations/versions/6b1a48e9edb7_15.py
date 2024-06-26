"""15

Revision ID: 6b1a48e9edb7
Revises: 8299a19ab1fa
Create Date: 2024-05-26 16:16:22.536223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b1a48e9edb7'
down_revision = '8299a19ab1fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('exercise', schema=None) as batch_op:
        batch_op.add_column(sa.Column('push_pull', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('difficulty', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('img', sa.String(), nullable=True))

    with op.batch_alter_table('exercise_log', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('exercise_log', schema=None) as batch_op:
        batch_op.drop_column('image_url')

    with op.batch_alter_table('exercise', schema=None) as batch_op:
        batch_op.drop_column('img')
        batch_op.drop_column('difficulty')
        batch_op.drop_column('push_pull')

    # ### end Alembic commands ###
