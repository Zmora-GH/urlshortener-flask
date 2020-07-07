"""shortURLs table

Revision ID: f5b45695a8bc
Revises: 
Create Date: 2020-07-07 18:15:42.204418

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5b45695a8bc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shortURL',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_url', sa.String(length=120), nullable=True),
    sa.Column('short_url', sa.String(length=32), nullable=True),
    sa.Column('clicks', sa.Integer(), nullable=True),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_shortURL_full_url'), 'shortURL', ['full_url'], unique=True)
    op.create_index(op.f('ix_shortURL_short_url'), 'shortURL', ['short_url'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_shortURL_short_url'), table_name='shortURL')
    op.drop_index(op.f('ix_shortURL_full_url'), table_name='shortURL')
    op.drop_table('shortURL')
    # ### end Alembic commands ###