# ==============================
# NODO BASE DEL AST
# ==============================

class NodoAST:
    def mostrar(self, nivel=0):
        print(" " * nivel + self.__class__.__name__)


# ==============================
# PRINT
# ==============================

class Print(NodoAST):
    def __init__(self, expresion):
        self.expresion = expresion

    def mostrar(self, nivel=0):
        print(" " * nivel + "Print -> " + str(self.expresion))


# ==============================
# PRINTLN
# ==============================

class Println(NodoAST):
    def __init__(self, expresion):
        self.expresion = expresion

    def mostrar(self, nivel=0):
        print(" " * nivel + "Println -> " + str(self.expresion))


# ==============================
# IF - ELSE
# ==============================

class If(NodoAST):
    def __init__(self, condicion, bloque_if, bloque_else=None):
        self.condicion = condicion
        self.bloque_if = bloque_if
        self.bloque_else = bloque_else

    def mostrar(self, nivel=0):
        print(" " * nivel + "If")
        print(" " * (nivel+2) + "Condición -> " + str(self.condicion))

        print(" " * (nivel+2) + "Bloque IF:")
        for instruccion in self.bloque_if:
            instruccion.mostrar(nivel+4)

        if self.bloque_else:
            print(" " * (nivel+2) + "Bloque ELSE:")
            for instruccion in self.bloque_else:
                instruccion.mostrar(nivel+4)


# ==============================
# WHILE
# ==============================

class While(NodoAST):
    def __init__(self, condicion, cuerpo):
        self.condicion = condicion
        self.cuerpo = cuerpo

    def mostrar(self, nivel=0):
        print(" " * nivel + "While")
        print(" " * (nivel+2) + "Condición -> " + str(self.condicion))

        print(" " * (nivel+2) + "Cuerpo:")
        for instruccion in self.cuerpo:
            instruccion.mostrar(nivel+4)


# ==============================
# FOR
# ==============================

class For(NodoAST):
    def __init__(self, variable, inicio, fin, cuerpo):
        self.variable = variable
        self.inicio = inicio
        self.fin = fin
        self.cuerpo = cuerpo

    def mostrar(self, nivel=0):
        print(" " * nivel + "For")
        print(" " * (nivel+2) + f"Variable -> {self.variable}")
        print(" " * (nivel+2) + f"Inicio -> {self.inicio}")
        print(" " * (nivel+2) + f"Fin -> {self.fin}")

        print(" " * (nivel+2) + "Cuerpo:")
        for instruccion in self.cuerpo:
            instruccion.mostrar(nivel+4)


# ==============================
# PROGRAMA DE EJEMPLO
# ==============================

programa = [

    Print("Hola mundo"),

    If(
        "x > 5",
        [Print("x es mayor que 5")],
        [Print("x es menor o igual a 5")]
    ),

    While(
        "x < 10",
        [Print("valor de x")]
    ),

    For(
        "i",
        0,
        5,
        [Println("i")]
    )
]


# ==============================
# MOSTRAR EL AST
# ==============================

print("ÁRBOL DE SINTAXIS ABSTRACTA\n")

for instruccion in programa:
    instruccion.mostrar()