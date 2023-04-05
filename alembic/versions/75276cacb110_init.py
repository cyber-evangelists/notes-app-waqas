"""init

Revision ID: 75276cacb110
Revises: 
Create Date: 2023-04-05 11:14:25.266929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75276cacb110'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'notes',
        sa.column('id', sa.Integer, primary_key=True),
        sa.column('title', sa.String, nullable=False),
        sa.column('description', sa.String, nullable=False),
        sa.column('url', sa.String, nullable=True)
    )


def downgrade():
    op.drop_table('notes')
