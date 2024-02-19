""" Utilizando clases creo algo basico de seguimiento y seguidores en instagram """


class Usuario:

    def __init__(self, usuario_id, nombreusuario):
        self.id = usuario_id
        self.nombreusuario = nombreusuario
        self.seguidores = 0
        self.seguimiento = 0

    def seguir(self, usuario):
        usuario.seguidores += 1
        self.seguimiento += 1


usuario_1 = Usuario("001", "Juan")
usuario_2 = Usuario("002", "Nieves")
usuario_3 = Usuario("003", "Carlos")
usuario_4 = Usuario("004", "Ester")

usuario_1.seguir(usuario_2)
usuario_3.seguir(usuario_2)
print(usuario_1.seguidores)
print(usuario_1.seguimiento)

print(usuario_2.seguidores)
print(usuario_2.seguimiento)
