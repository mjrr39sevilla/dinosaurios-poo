from src.models.dinosaurio import Dinosaurio


class TRex(Dinosaurio):
    def emitir_sonido(self):
        return "¡ROAAAR!"

    def moverse(self):
        return "camina sobre dos patas"
