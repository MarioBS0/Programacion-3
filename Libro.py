class Libro():
    __Tamaño = "17x24"
    Paginas = 0
    PrecioVenta = 0
    Peso = 0
    __PrecioxPag = 0
    __PesoxPag = 0
    Titulo = ""
    Tapa = ""
    URL = ""
    ISBN = ""
    Estado = "No Registrado"

    def __init__(self):
        self.__Tamaño = "17x24"
        self.__PrecioxPag = 300
        self.__PesoxPag = 0.8
    
    def RegistrarLibro(self):
        self.Estado = "Registrado"
        return self.Estado
    
    def PrecioxPagina(self):
        return self.__PrecioxPag
    
    def PesoxPagina(self):
        return self.__PesoxPag
    
    def TamañoLibro(self):
        return self.__Tamaño
    
    def DatosLibro(self, NumPags, Nombre, TipoTapa, URLLibro, ISBNLibro):
        self.Paginas = NumPags
        self.PrecioVenta = self.PrecioxPagina() * NumPags
        self.Peso = self.PesoxPagina() * NumPags
        self.Titulo = Nombre
        self.Tapa = TipoTapa
        self.URL = URLLibro
        self.ISBN = ISBNLibro

    def RecibeDatosLibro(self):
        Nombre = input("Titulo Libro: ")
        NumPags = int(input("Numero de Paginas: "))
        TipoTapa = input("Tapa Dura (D), Tapa Blanda (B): ")
        URLLibro = input("URL? (Si/No): ")
        ISBNLibro = input("ISBN: ")

        print("***********************************************************************")
        self.DatosLibro(NumPags, Nombre, TipoTapa, URLLibro, ISBNLibro)

    def MuestraDatosLibro(self):
        print("Tamaño= ", self.TamañoLibro())
        print("Paginas= ", self.Paginas)
        print("Precio Venta= ", self.PrecioVenta, "COP")
        print("Peso= ", round(self.Peso, 2), "gms")
        print("PrecioxPag= ", round(self.PrecioxPagina(), 2))
        print("PesoxPag= ", self.PesoxPagina())
        print("Titulo= ", self.Titulo)
        print("Tapa= ", self.Tapa)
        print("URL= ", self.URL)
        print("Estado= ", self.Estado)
        print("*************************************************************************")

Libro1 = Libro()
Libro2 = Libro()

print("DATOS LIBRO 1")
Libro1.RecibeDatosLibro()

print("DATOS LIBRO 2")
Libro2.RecibeDatosLibro()

Libro1.MuestraDatosLibro()
Libro2.MuestraDatosLibro()

