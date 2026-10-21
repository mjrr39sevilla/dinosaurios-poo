from src.models.dinosaurio import Dinosaurio


class Triceratops(Dinosaurio):
    def emitir_sonido(self):
        return "¡Muuuh!"

    def moverse(self):
        return "avanza embistiendo"
