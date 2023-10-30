import pyodbc
from data.clsDatos import clsDatos

class clsConexion():
    # Declare the variables for the connection
    _servidor = 'DESKTOP-KIMF180'
    _basedatos = 'datos'

    def __init__(self):
        pass

    def _conectar(self):
        try:
            _conex = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                   'SERVER=' + self._servidor +
                                   ';DATABASE=' + self._basedatos +
                                   ';Trusted_Connection=yes')  # Use Windows Authentication
        except Exception as err:
            print(err)
        return _conex

    def agregars(self, dato):
        estado = False
        AuxSql = "INSERT INTO datos (texto, descripcion) VALUES (?, ?)"
        try:
            _conex = self._conectar()
            with _conex.cursor() as cursor:
                cursor.execute(AuxSql, (dato.Texto, dato.Descripcion))
                _conex.commit()  # Commit the transaction

            estado = True
        except Exception as err:
            print(f"Error while adding data: {err}")
        finally:
            _conex.close()
        return estado

    def agregarUsuario(self, user):
        estado = False
        AuxSql = "INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)"
        try:
            _conex = self._conectar()
            with _conex.cursor() as cursor:
                cursor.execute(AuxSql, (user.Usuarios, user.Contrasena))
                _conex.commit()  # Commit the transaction

            estado = True
        except Exception as err:
            print(f"Error while adding data: {err}")
        finally:
            _conex.close()
        return estado


    def editar(self, dato):
        estado = False
        AuxSql = "update datos set texto = '{1}', descripcion = '{2}' where id = {0}".format(dato.ID, dato.Texto, dato.Descripcion)
        try:
            _conex = self._conectar()
            with _conex.cursor() as cursor:
                cursor.execute(AuxSql)

            _conex.close()
            estado = True
        except Exception as err:
            print(err)
        return estado


    def borrar(self, ide):
        estado = False
        AuxSql = "delete datos where id = {0}".format(ide)
        try:
            _conex = self._conectar()
            with _conex.cursor() as cursor:
                cursor.execute(AuxSql)

            _conex.close()
            estado = True
        except Exception as err:
            print(err)
        return estado


    def consultar(self, ide=None):
        data = ''
        salida = []

        try:
            _conex = self._conectar()
            with _conex.cursor() as cursor:
                if ide is None:
                    cursor.execute("Select * from datos")
                else:
                    cursor.execute("Select * from datos where id = {0}".format(ide))
                data = cursor.fetchall()

            _conex.close()
        except Exception as err:
            print(err)

        for tupla in data:
            salida.append(clsDatos(tupla[0], tupla[1], tupla[2]))

        return salida