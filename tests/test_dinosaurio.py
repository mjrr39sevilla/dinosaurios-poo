import pytest

from src.models.dinosaurio import Dinosaurio
from src.models.trex import TRex
from src.models.velociraptor import Velociraptor
from src.models.triceratops import Triceratops
from src.models.brachiosaurus import Brachiosaurus
from src.models.parque import Parque


# --- Abstracción ---
def test_dinosaurio_no_se_puede_instanciar():
    with pytest.raises(TypeError):
        Dinosaurio("Genérico", 100)


# --- Herencia ---
@pytest.mark.parametrize("clase", [TRex, Velociraptor, Triceratops, Brachiosaurus])
def test_subclases_heredan_de_dinosaurio(clase):
    assert issubclass(clase, Dinosaurio)
    assert isinstance(clase("Test", 100), Dinosaurio)


# --- Polimorfismo ---
@pytest.mark.parametrize(
    "clase, sonido, movimiento",
    [
        (TRex, "¡ROAAAR!", "camina sobre dos patas"),
        (Velociraptor, "¡Skrii!", "corre a toda velocidad"),
        (Triceratops, "¡Muuuh!", "avanza embistiendo"),
        (Brachiosaurus, "¡Fuuuum!", "camina despacio"),
    ],
)
def test_cada_subclase_se_comporta_a_su_manera(clase, sonido, movimiento):
    dino = clase("Test", 100)
    assert dino.emitir_sonido() == sonido
    assert dino.moverse() == movimiento


# --- Encapsulación ---
def test_describir():
    assert TRex("Rexy", 8000).describir() == "Rexy (8000 kg)"


def test_peso_se_puede_modificar_con_setter():
    dino = TRex("Rexy", 8000)
    dino.peso = 8500
    assert dino.peso == 8500


def test_peso_invalido_lanza_error():
    dino = TRex("Rexy", 8000)
    with pytest.raises(ValueError):
        dino.peso = 0


# --- Parque ---
def test_anadir_dinosaurio_al_parque(capsys):
    parque = Parque("Isla Nublar")
    parque.anadir_dinosaurio(Velociraptor("Blue", 90))
    parque.listar_dinosaurios()
    salida = capsys.readouterr().out
    assert "Isla Nublar" in salida
    assert "Blue (90 kg)" in salida


def test_parque_rechaza_objetos_que_no_son_dinosaurios():
    parque = Parque("Isla Nublar")
    with pytest.raises(TypeError):
        parque.anadir_dinosaurio("no soy un dinosaurio")
