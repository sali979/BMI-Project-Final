from datetime import date, datetime, datetime_CAPI
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    ForeignKey,
    event,
    Float,
)
from sqlalchemy.orm import mapper, relationship

import domain.health_record


metadata = MetaData()

user_records = Table(
    "user_records",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("category", String(255)),
    Column("bmi", Float, nullable=False),
    Column("username", String(255)),
)

health_records = Table(
    "health_records",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("username", String(255), nullable=False),
    Column("height", Float, nullable=False),
    Column("weight", Float, nullable=False),
    Column("gender", String(1), nullable=False),
    Column("date_of_birth", String, nullable=True),
    Column("bmi", Float, nullable=False)

)

allocations = Table(
    "allocations",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", ForeignKey("user_records.id")),
    Column("healthrecord_id", ForeignKey("health_records.id")),
)


def start_mappers():
    urecords_mapper = mapper(health_record.UserRecord, user_records)
    mapper(
        health_record.HealthRecord,
        health_records,
        properties={
            "_allocations": relationship(
                urecords_mapper, secondary=allocations, collection_class=set,
            )
        },
    )
