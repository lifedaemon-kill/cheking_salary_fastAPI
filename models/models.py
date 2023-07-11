from uuid import UUID
from datetime import utcnow
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey

metadata = MetaData()

salary = Table(
    "salary",
    metadata,
    Column("id", UUID, primary_key=True),
    Column("sum", Integer, nullable=False),
    Column("date_increase", TIMESTAMP, nullable=False),
)

employees = Table(
    "employees",
    metadata,
    Column("id", UUID, primary_key=True),
    Column("login", String, nullable=False),
    Column("password", String,  nullable=False),
    Column("registered_at", TIMESTAMP, default=utcnow),
    Column("salary_id", Integer, ForeignKey("salary.id"))
)
