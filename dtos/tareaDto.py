from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.tareas import TareaModel

class TareaRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        model = TareaModel
        # cuando nosotros cramos un DTO este solamente servira para las columnas de ese modelo pero sin ninguna llave faranea
        # se queremos utilizar tambien las llaves faraneas:
        include_fk = True