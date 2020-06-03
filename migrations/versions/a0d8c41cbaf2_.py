"""empty message

Revision ID: a0d8c41cbaf2
Revises: 
Create Date: 2020-06-02 21:36:20.376365

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0d8c41cbaf2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('actor', sa.Column('age', sa.Integer(), nullable=True))
    op.add_column('actor', sa.Column('gender', sa.String(), nullable=True))
    op.add_column('actor', sa.Column('name', sa.String(), nullable=True))
    op.add_column('actor_movie', sa.Column('actor_id', sa.Integer(), nullable=True))
    op.add_column('actor_movie', sa.Column('movie_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'actor_movie', 'movie', ['movie_id'], ['id'])
    op.create_foreign_key(None, 'actor_movie', 'actor', ['actor_id'], ['id'])
    op.add_column('movie', sa.Column('release_date', sa.Date(), nullable=True))
    op.add_column('movie', sa.Column('title', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movie', 'title')
    op.drop_column('movie', 'release_date')
    op.drop_constraint(None, 'actor_movie', type_='foreignkey')
    op.drop_constraint(None, 'actor_movie', type_='foreignkey')
    op.drop_column('actor_movie', 'movie_id')
    op.drop_column('actor_movie', 'actor_id')
    op.drop_column('actor', 'name')
    op.drop_column('actor', 'gender')
    op.drop_column('actor', 'age')
    # ### end Alembic commands ###
