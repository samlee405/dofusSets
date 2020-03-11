"""empty message

Revision ID: 4e7f099d776b
Revises: 81f1b88a96c7
Create Date: 2020-02-17 20:59:45.766354

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "4e7f099d776b"
down_revision = "81f1b88a96c7"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "custom_set_exo",
        "stat",
        existing_type=postgresql.ENUM(
            "VITALITY",
            "AP",
            "MP",
            "INITIATIVE",
            "PROSPECTING",
            "RANGE",
            "SUMMON",
            "WISDOM",
            "STRENGTH",
            "INTELLIGENCE",
            "CHANCE",
            "AGILITY",
            "AP_PARRY",
            "AP_REDUCTION",
            "MP_PARRY",
            "MP_REDUCTION",
            "CRITICAL",
            "HEALS",
            "LOCK",
            "DODGE",
            "PCT_FINAL_DAMAGE",
            "POWER",
            "DAMAGE",
            "CRITICAL_DAMAGE",
            "NEUTRAL_DAMAGE",
            "EARTH_DAMAGE",
            "FIRE_DAMAGE",
            "WATER_DAMAGE",
            "AIR_DAMAGE",
            "REFLECT",
            "TRAP_DAMAGE",
            "TRAP_POWER",
            "PUSHBACK_DAMAGE",
            "PCT_SPELL_DAMAGE",
            "PCT_WEAPON_DAMAGE",
            "PCT_RANGED_DAMAGE",
            "PCT_MELEE_DAMAGE",
            "NEUTRAL_RES",
            "PCT_NEUTRAL_RES",
            "EARTH_RES",
            "PCT_EARTH_RES",
            "FIRE_RES",
            "PCT_FIRE_RES",
            "WATER_RES",
            "PCT_WATER_RES",
            "AIR_RES",
            "PCT_AIR_RES",
            "CRITICAL_RES",
            "PUSHBACK_RES",
            "PCT_RANGED_RES",
            "PCT_MELEE_RES",
            "PODS",
            name="stat",
        ),
        nullable=True,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "custom_set_exo",
        "stat",
        existing_type=postgresql.ENUM(
            "VITALITY",
            "AP",
            "MP",
            "INITIATIVE",
            "PROSPECTING",
            "RANGE",
            "SUMMON",
            "WISDOM",
            "STRENGTH",
            "INTELLIGENCE",
            "CHANCE",
            "AGILITY",
            "AP_PARRY",
            "AP_REDUCTION",
            "MP_PARRY",
            "MP_REDUCTION",
            "CRITICAL",
            "HEALS",
            "LOCK",
            "DODGE",
            "PCT_FINAL_DAMAGE",
            "POWER",
            "DAMAGE",
            "CRITICAL_DAMAGE",
            "NEUTRAL_DAMAGE",
            "EARTH_DAMAGE",
            "FIRE_DAMAGE",
            "WATER_DAMAGE",
            "AIR_DAMAGE",
            "REFLECT",
            "TRAP_DAMAGE",
            "TRAP_POWER",
            "PUSHBACK_DAMAGE",
            "PCT_SPELL_DAMAGE",
            "PCT_WEAPON_DAMAGE",
            "PCT_RANGED_DAMAGE",
            "PCT_MELEE_DAMAGE",
            "NEUTRAL_RES",
            "PCT_NEUTRAL_RES",
            "EARTH_RES",
            "PCT_EARTH_RES",
            "FIRE_RES",
            "PCT_FIRE_RES",
            "WATER_RES",
            "PCT_WATER_RES",
            "AIR_RES",
            "PCT_AIR_RES",
            "CRITICAL_RES",
            "PUSHBACK_RES",
            "PCT_RANGED_RES",
            "PCT_MELEE_RES",
            "PODS",
            name="stat",
        ),
        nullable=False,
    )
    # ### end Alembic commands ###
