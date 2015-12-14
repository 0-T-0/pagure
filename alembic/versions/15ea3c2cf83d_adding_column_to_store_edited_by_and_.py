"""Adding column to store edited_by and edited_on a comment

Revision ID: 15ea3c2cf83d
Revises: 1cd0a853c697
Create Date: 2015-11-09 16:18:47.192088

"""

# revision identifiers, used by Alembic.
revision = '15ea3c2cf83d'
down_revision = '1cd0a853c697'

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.add_column(
        'pull_request_comments',
        sa.Column(
            'editor_id',
            sa.Integer,
            sa.ForeignKey('users.id', onupdate='CASCADE'),
            nullable=True)
    )

    op.add_column(
        'pull_request_comments',
        sa.Column(
            'edited_on',
            sa.DateTime,
            nullable=True)
    )


def downgrade():
    op.drop_column('pull_request_comments', 'editor_id')
    op.drop_column('pull_request_comments', 'edited_on')
