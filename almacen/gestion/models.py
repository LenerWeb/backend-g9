from django.db import models

class DepartamentoModel(models.Model):
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/
    # declaramos las columnas de este modelo
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-types
    # si nosotros nos declaramos AutoField, Django de manera predeterminada creara una columna llamada id que sera autoincrementable
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-options > mostrarme todas las opciones que le puedo colocar a todas las columnas
    id= models.AutoField(primary_key=True, unique=True, null=False)
    nombre= models.CharField(max_length=50, null=False)
    codigo_postal = models.CharField(max_length=10, unique=True, db_column='codigo_postal')

    class Meta:
        # pasarle metadta o informacion adicional a la clase de la cuela estamos heredando
        # https://docs.djangoproject.com/en/4.1/ref/models/options/
        db_table = 'departamentos'

class AlmacenModel(models.Model):
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#choices
    # see declara uiuna lista de tuplas en la cuela el primer valor de cada tupla sera lo que se guardara en la base de datos, mientras que el segundo valor sera lo que el usuario leera al devolver la informacion
    # UTILIZANDO UNA LISTA DE TUPLAS
    tipoAlmacen = [
        ('A','SECO'),
        ('B','SEMI-SECO'),
        ('C','HUMEDO')
    ]
    # FORMA UTILIZANDO CLASES
    class TipoAlmacenesOpciones(models.TextChoices):
        SECO = ('A','SECO')
        SEMISECO = ('B','SEMI-SECO')
        HUMEDO = ('C','HUMEDO')
    # no se va a crear la columna id
    # db_column > indicara como se va a llamar esta columna en la base de datos, si no se le indica sera el nombre del atributo
    espacioAnaquel = models.IntegerField(db_column='espacio_anaquel')
    tipo = models.CharField(max_length=100, choices=tipoAlmacen)
    # tipo = models.CharField(max_length=100, choices=TipoAlmacenesOpciones.choices)
    direccion = models.CharField(max_length=250)
    # REKLACIONES ONE-TO-ONE
    # on_delete > se guardara la informacion de como debe actuar el almacen si es que se elimina el departamento ( el registro con ese modelo)
    # CASCADE > se elimina el departamento y en forma de cascada se elimina el almancen
    # PROTECT > evita la eliminacion y lanza un error de tipo ProtectedError
    # RESTRIC > muy similar al PROTECT pero emite un error de tipo RestrictedError
    #SET_NULL > elimina el departamento y a este valor lo cambia a null
    #SET_DEFAULT > elimina el departamento perio tenemos que indicar uin calor por default para que le camvbie a ese valor
    # DO_NOTHING > elimina el departamento pero conserva el valor (FK) copn lo que genera una mala integridad de informacion NO USAR ESTE porque malogra la calidad de la data
    departamento = models.OneToOneField(to=DepartamentoModel, on_delete=models.CASCADE, db_column='departamento_id')

    class Meta:
        # db_table > indica como se llamara esta tabla en la base de datos, si no le indicamos usara el nombre de la clase como nombre de tabla
        db_table = 'almacenes'
        # ordering > modificara el ordenamiento natural al momento de devolver varios registros, si se le pone un '-' al comienzo entonces se indicara que sera descendiente, caso contrario ascendente
        ordering = ['-espacioAnaquel', 'direccion']
        # unique_together > crear una unicidad compuesta, esto significaque los valores de dos culumnas no se puede repetir
        unique_together = [['direccion','tipo']]