# 🦖 Dinosaurios POO

Proyecto desarrollado en **Python** para practicar los fundamentos de la Programación Orientada a Objetos (POO) mediante la creación de diferentes especies de dinosaurios y su gestión dentro de un parque.

## 📋 Descripción del proyecto

La aplicación permite crear dinosaurios con características y comportamientos propios, incorporarlos a un parque y mostrar información sobre cada uno de ellos.

El proyecto utiliza una clase abstracta como base para definir las características comunes de los dinosaurios y clases derivadas que implementan sus propios sonidos y formas de desplazamiento.

## 🎯 Objetivos

- Practicar los principios fundamentales de la Programación Orientada a Objetos.
- Implementar clases abstractas, herencia y polimorfismo.
- Aplicar encapsulación mediante propiedades.
- Establecer relaciones entre objetos.
- Validar datos y controlar errores.
- Desarrollar pruebas automatizadas con `pytest`.

## 🦕 Dinosaurios implementados

| Clase | Comportamiento |
|---|---|
| `TRex` | Camina sobre dos patas y emite un rugido. |
| `Velociraptor` | Corre a toda velocidad y emite su sonido característico. |
| `Triceratops` | Avanza embistiendo y emite su sonido. |
| `Brachiosaurus` | Camina despacio y emite su sonido. |

Todas las especies heredan de la clase abstracta `Dinosaurio`.

## 🧠 Conceptos de POO aplicados

**Abstracción**

La clase `Dinosaurio` define los métodos abstractos `emitir_sonido()` y `moverse()`, que deben implementar las clases derivadas.

**Herencia**

Las clases concretas heredan de `Dinosaurio` las propiedades y los métodos comunes.

**Encapsulación**

Se utilizan atributos internos y propiedades para acceder al nombre y al peso. Además, el peso debe ser mayor que cero.

**Polimorfismo**

Cada dinosaurio implementa sus propios sonidos y movimientos. El parque puede trabajar con diferentes especies utilizando los mismos métodos.

**Relación entre objetos**

La clase `Parque` contiene una colección de dinosaurios y permite añadirlos y mostrarlos.

## 📁 Estructura del proyecto

```text
dinosaurios-poo/
├── main.py
├── pyproject.toml
├── README.md
├── .gitignore
├── src/
│   ├── __init__.py
│   └── models/
│       ├── dinosaurio.py
│       ├── parque.py
│       ├── trex.py
│       ├── velociraptor.py
│       ├── triceratops.py
│       └── brachiosaurus.py
└── tests/
    └── test_dinosaurio.py
```

## ⚙️ Requisitos

- Python 3.11 o superior.
- `pytest` para ejecutar las pruebas automatizadas.
- Un entorno virtual recomendado para aislar las dependencias.

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/mjrr39sevilla/dinosaurios-poo.git
cd dinosaurios-poo
```

### 2. Crear un entorno virtual

En Windows:

```powershell
python -m venv .venv
```

### 3. Activar el entorno virtual

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar pytest

```powershell
python -m pip install pytest
```

### 5. Ejecutar la aplicación

Desde la raíz del proyecto:

```powershell
python main.py
```

La aplicación crea el parque Isla Nublar, incorpora cuatro dinosaurios y muestra sus nombres, pesos, sonidos y movimientos.

## 🧪 Pruebas automatizadas

El proyecto utiliza `pytest` para comprobar el funcionamiento de las clases y sus comportamientos.

Para ejecutar todas las pruebas:

```powershell
python -m pytest -v
```

Las pruebas verifican:

- La abstracción de la clase `Dinosaurio`.
- Las propiedades y la validación del peso.
- La descripción de los dinosaurios.
- Los sonidos y movimientos de cada especie.
- La creación y gestión del parque.
- La validación de los objetos añadidos.
- El listado de los dinosaurios.

**Resultado obtenido:** 13 pruebas superadas (`13 passed`).

## 🛠️ Tecnologías utilizadas

- **Python:** lenguaje de programación.
- **Programación Orientada a Objetos:** organización del código mediante clases y objetos.
- **pytest:** framework de pruebas automatizadas.
- **Git y GitHub:** control de versiones y alojamiento del repositorio.

## 👩‍💻 Autora

Proyecto educativo desarrollado por **María José Rodríguez Ramos** como práctica de Programación Orientada a Objetos con Python.

---

*Proyecto de aprendizaje centrado en el diseño de clases, la reutilización del código y las pruebas automatizadas.*