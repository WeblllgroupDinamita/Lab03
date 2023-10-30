class clsUsuarios:
    def __init__(self, id=None, usuarios=None, contrasena=None):
        self._id = id
        self.usuarios = usuarios
        self._contrsasena = contrasena

    @property
    def ID(self):
        return self._id

    @ID.setter
    def ID(self, id):
        self._id = id

    @property
    def Usuarios(self):
        return self.usuarios

    @Usuarios.setter
    def Usuarios(self, usuarios):
        self.usuarios = usuarios

    @property
    def Contrasena(self):
        return self.contrasena

    @Contrasena.setter
    def Contrasena(self, contrasena):
        self.contrasena = contrasena

