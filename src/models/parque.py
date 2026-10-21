from src.models.dinosaurio import Dinosaurio


class Parque:
    """Relación "vive en": un parque contiene varios dinosaurios."""

    def __init__(self, nombre):
        self._nombre = nombre
        self._dinosaurios = []

    @property
    def nombre(self):
        return self._nombre

    def anadir_dinosaurio(self, dino):
        if not isinstance(dino, Dinosaurio):
            raise TypeError("Solo se pueden añadir dinosaurios")
        self._dinosaurios.append(dino)

    def listar_dinosaurios(self):
        print(f"--- {self._nombre} ---")
        for d in self._dinosaurios:
            print(f"{d.describir()} | {d.emitir_sonido()} | {d.moverse()}")
