
import pytest

from src.models.dinosaurio import Dinosaurio
from src.models.parque import Parque
from src.models.trex import TRex
from src.models.velociraptor import Velociraptor
from src.models.triceratops import Triceratops
from src.models.brachiosaurus import Brachiosaurus


def test_dinosaurio_es_abstracto():
    with pytest.raises(TypeError):
        Dinosaurio("Dino", 100)


def test_dinosaurio_propiedades():
    dino = TRex("Rexy", 8000)

    assert dino.nombre == "Rexy"
    assert dino.peso == 8000


def test_dinosaurio_modificar_peso():
    dino = TRex("Rexy", 8000)

    dino.peso = 8500

    assert dino.peso == 8500


def test_dinosaurio_peso_no_valido():
    dino = TRex("Rexy", 8000)

    with pytest.raises(ValueError):
        dino.peso = 0

    with pytest.raises(ValueError):
        dino.peso = -100


def test_dinosaurio_describir():
    dino = TRex("Rexy", 8000)

    assert dino.describir() == "Rexy (8000 kg)"


def test_trex():
    dino = TRex("Rexy", 8000)

    assert dino.emitir_sonido() == "¡ROAAAR!"
    assert dino.moverse() == "camina sobre dos patas"


def test_velociraptor():
    dino = Velociraptor("Blue", 90)

    assert dino.emitir_sonido() == "¡Skrii!"
    assert dino.moverse() == "corre a toda velocidad"


def test_triceratops():
    dino = Triceratops("Cuernos", 6000)

    assert dino.emitir_sonido() == "¡Muuuh!"
    assert dino.moverse() == "avanza embistiendo"


def test_brachiosaurus():
    dino = Brachiosaurus("Bracky", 30000)

    assert dino.emitir_sonido() == "¡Fuuuum!"
    assert dino.moverse() == "camina despacio"


def test_parque_nombre():
    parque = Parque("Isla Nublar")

    assert parque.nombre == "Isla Nublar"


def test_parque_anadir_dinosaurio():
    parque = Parque("Isla Nublar")
    dino = TRex("Rexy", 8000)

    parque.anadir_dinosaurio(dino)

    assert len(parque._dinosaurios) == 1
    assert parque._dinosaurios[0] is dino


def test_parque_rechaza_objetos_que_no_son_dinosaurios():
    parque = Parque("Isla Nublar")

    with pytest.raises(TypeError):
        parque.anadir_dinosaurio("No soy un dinosaurio")


def test_parque_listar_dinosaurios(capsys):
    parque = Parque("Isla Nublar")
    parque.anadir_dinosaurio(TRex("Rexy", 8000))

    parque.listar_dinosaurios()

    resultado = capsys.readouterr()

    assert "--- Isla Nublar ---" in resultado.out
    assert "Rexy (8000 kg)" in resultado.out
    assert "¡ROAAAR!" in resultado.out
    assert "camina sobre dos patas" in resultado.out
