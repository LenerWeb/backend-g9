from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.usuarios import UsuarioModel

class UsuarioRequestDto(SQLAlchemyAutoSchema):
    # pasar atributos a la clase que estamos heredando
    class Meta:
        #Esta clase permitira definir  atributos necesarios para la clase que estamos heredando
        #model > estamos indicando a SQLAlchemyAutoSchema cual sera el model que tiene que utilizar para generar las validaciones necesarias
        model= UsuarioModel