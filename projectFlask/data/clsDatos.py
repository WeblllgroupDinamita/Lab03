class clsDatos:
    def __init__(self, id=None, texto=None, descripcion=None):
        self._id = id
        self._text = texto
        self._descrip = descripcion
    @property
    def ID(self):
        return self._id

    @ID.setter
    def ID(self, id):
        self._id = id

    @property
    def Texto(self):
        return self._text

    @Texto.setter
    def Texto(self, texto):
        self._text = texto

    @property
    def Descripcion(self):
        return self._descrip

    @Descripcion.setter
    def Descripcion(self, descripcion):
        self._descrip = descripcion



