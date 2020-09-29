"""Initial migration.

Revision ID: cedb26bf96c9
Revises: 
Create Date: 2020-09-27 09:39:19.613354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "cedb26bf96c9"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "event",
        sa.Column("_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint("_id"),
        sa.UniqueConstraint("_id"),
        sa.UniqueConstraint("title"),
    )
    op.create_table(
        "metadata",
        sa.Column("sector", sa.String(length=50), nullable=False),
        sa.Column("indicator", sa.String(length=1000), nullable=False),
        sa.Column("definition", sa.String(length=2000), nullable=True),
        sa.Column("unit", sa.String(length=30), nullable=True),
        sa.Column("method", sa.String(length=500), nullable=True),
        sa.Column("compilation", sa.String(length=1000), nullable=True),
        sa.Column("source", sa.String(length=200), nullable=True),
        sa.Column("disaggregation", sa.String(length=100), nullable=True),
        sa.Column("accessibility", sa.String(length=100), nullable=True),
        sa.Column("periodicity", sa.String(length=100), nullable=True),
        sa.Column("comments", sa.String(length=100), nullable=True),
        sa.PrimaryKeyConstraint("indicator"),
        sa.UniqueConstraint("indicator"),
    )
    op.create_table(
        "news",
        sa.Column("_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=100), nullable=False),
        sa.Column("content", sa.String(length=20000), nullable=False),
        sa.PrimaryKeyConstraint("_id"),
        sa.UniqueConstraint("_id"),
        sa.UniqueConstraint("content"),
        sa.UniqueConstraint("title"),
    )
    op.create_table(
        "publications",
        sa.Column("_id", sa.Integer(), nullable=False),
        sa.Column("doc_name", sa.String(length=150), nullable=False),
        sa.Column("date_added", sa.DateTime(), nullable=True),
        sa.Column("size", sa.Integer(), nullable=False),
        sa.Column("downloads", sa.Integer(), nullable=True),
        sa.Column("contents", sa.String(length=200000), nullable=False),
        sa.PrimaryKeyConstraint("_id"),
        sa.UniqueConstraint("_id"),
    )
    op.create_table(
        "sector",
        sa.Column("_id", sa.Integer(), nullable=False),
        sa.Column("npgei", sa.String(length=10), nullable=True),
        sa.Column("sector", sa.String(length=100), nullable=True),
        sa.Column("indicator", sa.String(length=500), nullable=True),
        sa.Column("source", sa.String(length=100), nullable=True),
        sa.Column("geo", sa.String(length=100), nullable=True),
        sa.Column("tier", sa.String(length=10), nullable=True),
        sa.Column("males_2013", sa.String(length=20), nullable=True),
        sa.Column("females_2013", sa.String(length=20), nullable=True),
        sa.Column("total_2013", sa.String(length=20), nullable=True),
        sa.Column("males_2014", sa.String(length=20), nullable=True),
        sa.Column("females_2014", sa.String(length=20), nullable=True),
        sa.Column("total_2014", sa.String(length=20), nullable=True),
        sa.Column("males_2015", sa.String(length=20), nullable=True),
        sa.Column("females_2015", sa.String(length=20), nullable=True),
        sa.Column("total_2015", sa.String(length=20), nullable=True),
        sa.Column("males_2016", sa.String(length=20), nullable=True),
        sa.Column("females_2016", sa.String(length=20), nullable=True),
        sa.Column("total_2016", sa.String(length=20), nullable=True),
        sa.Column("males_2017", sa.String(length=20), nullable=True),
        sa.Column("females_2017", sa.String(length=20), nullable=True),
        sa.Column("total_2017", sa.String(length=20), nullable=True),
        sa.Column("males_2021", sa.String(length=20), nullable=True),
        sa.Column("females_2021", sa.String(length=20), nullable=True),
        sa.Column("total_2021", sa.String(length=20), nullable=True),
        sa.PrimaryKeyConstraint("_id"),
        sa.UniqueConstraint("_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("sector")
    op.drop_table("publications")
    op.drop_table("news")
    op.drop_table("metadata")
    op.drop_table("event")
    # ### end Alembic commands ###
