""""delete_mountpoint_from_snapshot"

Revision ID: 541673c481bd
Revises: 60aad748b94b
Create Date: 2017-07-07 15:52:47.904384

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import Session
from sqlalchemy.sql import table, column
from rest_api_server.utils import Config

# revision identifiers, used by Alembic.
revision = '541673c481bd'
down_revision = '60aad748b94b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    mountpoints = Config().client.storages()
    mounpoint = mountpoints[0]
    mountpoint_table = table('mountpoint', column('mountpoint', sa.TEXT()))
    bind = op.get_bind()
    session = Session(bind=bind)
    upd_stmt = sa.update(mountpoint_table).values(mountpoint=mounpoint).where(mountpoint_table.c.mountpoint.is_(None))
    try:
        session.execute(upd_stmt)
        session.commit()
    finally:
        session.close()
    op.alter_column('mountpoint', 'mountpoint',
                    existing_type=sa.TEXT(),
                    nullable=False)
    op.drop_column('snapshot', 'mountpoint')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('snapshot', sa.Column('mountpoint', sa.String(length=256), nullable=True))
    op.alter_column('mountpoint', 'mountpoint',
                    existing_type=sa.TEXT(),
                    nullable=True)
    # ### end Alembic commands ###