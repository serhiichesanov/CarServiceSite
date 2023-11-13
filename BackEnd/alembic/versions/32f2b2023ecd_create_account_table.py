"""create tables

Revision ID: 32f2b2023ecd
Revises: 
Create Date: 2021-11-01 21:44:21.449494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32f2b2023ecd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("car",
                    sa.Column("id", sa.Integer, primary_key=True),
                    sa.Column("carMark", sa.VARCHAR(256), nullable=False),
                    sa.Column("carSpeed", sa.Integer, nullable=False),
                    sa.Column("carNumber", sa.Integer, nullable=False)
                    )

    op.create_table("user",
                    sa.Column("id", sa.Integer, primary_key=True),
                    sa.Column("username", sa.VARCHAR(256), nullable=False),
                    sa.Column("firstName", sa.VARCHAR(256), nullable=False),
                    sa.Column("lastName", sa.VARCHAR(256), nullable=False),
                    sa.Column("email", sa.VARCHAR(256), nullable=False),
                    sa.Column("password", sa.VARCHAR(256), nullable=False),
                    sa.Column("phone", sa.VARCHAR(256), nullable=False),
                    sa.Column("userStatus", sa.Boolean(), nullable=False)
                    )

    op.create_table("admin",
                    sa.Column("id", sa.Integer, primary_key=True),
                    sa.Column("userId", sa.Integer,
                              sa.ForeignKey("user.id",
                                            onupdate="CASCADE",
                                            ondelete="CASCADE"),
                              unique=True,
                              nullable=False),
                    sa.Column("adminRights",
                              sa.dialects.mysql.ENUM("employee",
                                                     "managment",
                                                     "owner"),
                              nullable=False)
                    )

    op.create_table("rent",
                    sa.Column("id", sa.Integer, primary_key=True),
                    sa.Column("userId", sa.Integer,
                              sa.ForeignKey("user.id",
                                            onupdate="CASCADE",
                                            ondelete="CASCADE"),
                              unique=False,
                              nullable=False),
                    sa.Column("carId", sa.Integer,
                              sa.ForeignKey("car.id",
                                            onupdate="CASCADE",
                                            ondelete="CASCADE"),
                              unique=False,
                              nullable=False),
                    sa.Column("startRent", sa.DateTime),
                    sa.Column("endRent", sa.DateTime),
                    sa.Column("totalPrice", sa.Float)
                    )


def downgrade():
    op.drop_table("rent")
    op.drop_table("admin")
    op.drop_table("car")
    op.drop_table("user")
    # op.drop_table("alembic_version")
