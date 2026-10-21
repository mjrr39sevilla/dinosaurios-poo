from src.models.dinosaurio import Dinosaurio


class Velociraptor(Dinosaurio):
    def emitir_sonido(self):
        return "¡Skrii!"

    def moverse(self):
        return "corre a toda velocidad"
