from src.models.parque import Parque
from src.models.trex import TRex
from src.models.velociraptor import Velociraptor
from src.models.triceratops import Triceratops
from src.models.brachiosaurus import Brachiosaurus


def main():
    parque = Parque("Isla Nublar")
    parque.anadir_dinosaurio(TRex("Rexy", 8000))
    parque.anadir_dinosaurio(Velociraptor("Blue", 90))
    parque.anadir_dinosaurio(Triceratops("Cuernos", 6000))
    parque.anadir_dinosaurio(Brachiosaurus("Bracky", 30000))
    parque.listar_dinosaurios()


if __name__ == "__main__":
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
