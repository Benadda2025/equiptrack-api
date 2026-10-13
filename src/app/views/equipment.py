from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface

from app.models.equipment import Equipment
from app import appbuilder


class EquipmentView(ModelView):
    datamodel = SQLAInterface(Equipment)

    list_columns = [
        "name",
        "serial_number",
        "status",
    ]

    show_columns = [
        "name",
        "serial_number",
        "status",
    ]


appbuilder.add_view(
    EquipmentView,
    "Equipment",
    icon="fa-laptop",
    category="Inventory",
)
