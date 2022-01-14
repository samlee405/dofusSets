"""empty message

Revision ID: b9b68fd74d2a
Revises: 4180ddd14d6a
Create Date: 2022-01-13 18:50:41.696776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b9b68fd74d2a"
down_revision = "4180ddd14d6a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "user_account",
        sa.Column("profile_picture", sa.String(length=120), nullable=True),
    )
    op.execute(
        "UPDATE user_account SET profile_picture = 'profile-pictures/ProPic_Emerald_1.png'"
    )
    op.alter_column("user_account", "profile_picture", nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user_account", "profile_picture")
    # ### end Alembic commands ###
