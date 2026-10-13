from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import relationship


class Equipment(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    serial_number = Column(String(100), unique=True, nullable=False)
    status = Column(
        SqlEnum("available", "assigned", "maintenance", name="equipment_status"),
        nullable=False,
        default="available",
    )

    # assignments = relationship(
    #     "Assignment", back_populates="equipment"
    # )
