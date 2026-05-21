"""Create telephone number for user column

Revision ID: c9193378eaee
Revises: 
Create Date: 2026-05-10 19:17:09.703888

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c9193378eaee'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('telephone_number', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'telephone_number')