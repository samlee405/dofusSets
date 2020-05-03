"""empty message

Revision ID: 761778ee8ca2
Revises: 9ce751fbce98
Create Date: 2020-05-02 23:29:50.356990

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "761778ee8ca2"
down_revision = "9ce751fbce98"
branch_labels = None
depends_on = None

url_base = "https://dofus-lab.s3.us-east-2.amazonaws.com/class/{}.png"


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("class", sa.Column("image_url", sa.String(), nullable=True))
    conn = op.get_bind()
    res = conn.execute(
        "SELECT c.uuid, ct.name FROM class c JOIN class_translation ct ON c.uuid = ct.class_id WHERE locale='en';"
    )
    classes = res.fetchall()
    for dofus_class in classes:
        conn.execute(
            "UPDATE class SET image_url='{}' WHERE uuid='{}'".format(
                url_base.format(dofus_class[1]), dofus_class[0]
            )
        )
    op.alter_column("class", "image_url", nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("class", "image_url")
    # ### end Alembic commands ###
