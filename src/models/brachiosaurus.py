from src.models.dinosaurio import Dinosaurio


class Brachiosaurus(Dinosaurio):
    def emitir_sonido(self):
        return "¡Fuuuum!"

    def moverse(self):
        return "camina despacio"
