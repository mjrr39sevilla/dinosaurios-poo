from abc import ABC, abstractmethod


class Dinosaurio(ABC):
    """Clase padre abstracta: define lo esencial de cualquier dinosaurio."""

    def __init__(self, nombre, peso):
        self._nombre = nombre
        self._peso = peso

    @property
    def nombre(self):
        return self._nombre

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, valor):
        if valor <= 0:
            raise ValueError("El peso debe ser mayor que 0")
        self._peso = valor

    def describir(self):
        return f"{self._nombre} ({self._peso} kg)"

    @abstractmethod
    def emitir_sonido(self):
        pass

    @abstractmethod
    def moverse(self):
        pass
