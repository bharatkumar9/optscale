""""budget_constraints"

Revision ID: fb929606710b
Revises: de2e74456ef3
Create Date: 2020-08-17 06:41:26.448594

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb929606710b'
down_revision = 'e0cde169e379'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'resource_constraint',
        sa.Column('id', sa.String(length=36), nullable=False),
        sa.Column('created_at', sa.Integer(), nullable=False),
        sa.Column('deleted_at', sa.Integer(), nullable=False),
        sa.Column('type', sa.Enum('TTL', 'EXPENSE_LIMIT'), nullable=False),
        sa.Column('limit', sa.Integer(), nullable=False),
        sa.Column('resource_id', sa.String(length=36), nullable=False),
        sa.ForeignKeyConstraint(['resource_id'], ['resource.id'],
                                name='constraint_resource_fk'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('type', 'resource_id', 'deleted_at',
                            name='uc_name_del_at_parent_id')
    )
    op.create_table(
        'budget_policy',
        sa.Column('id', sa.String(length=36), nullable=False),
        sa.Column('created_at', sa.Integer(), nullable=False),
        sa.Column('deleted_at', sa.Integer(), nullable=False),
        sa.Column('type', sa.Enum('TTL', 'EXPENSE_LIMIT'), nullable=False),
        sa.Column('limit', sa.Integer(), nullable=False),
        sa.Column('active', sa.Boolean(), nullable=False),
        sa.Column('budget_id', sa.String(length=36), nullable=False),
        sa.ForeignKeyConstraint(
            ['budget_id'], ['budget.id'], name='policy_budget_fk'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('type', 'budget_id', 'deleted_at',
                            name='uc_name_del_at_parent_id')
    )
    op.create_table(
        'constraint_limit_hit',
        sa.Column('id', sa.String(length=36), nullable=False),
        sa.Column('created_at', sa.Integer(), nullable=False),
        sa.Column('deleted_at', sa.Integer(), nullable=False),
        sa.Column('resource_id', sa.String(length=36), nullable=False),
        sa.Column('budget_id', sa.String(length=36), nullable=False),
        sa.Column('type', sa.Enum('TTL', 'EXPENSE_LIMIT'), nullable=False),
        sa.Column('constraint_limit', sa.Integer(), nullable=False),
        sa.Column('hit_value', sa.Integer(), nullable=False),
        sa.Column('time', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['budget_id'], ['budget.id'], name='limit_hit_budget_fk'),
        sa.ForeignKeyConstraint(
            ['resource_id'], ['resource.id'], name='limit_hit_resource_fk'),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('resource_constraint')
    op.drop_table('constraint_limit_hit')
    op.drop_table('budget_policy')
    # ### end Alembic commands ###