## Reto 06

`reservaciones/`

Organizar el programa de reservaciones, en un paquete con dos módulos: `entrada.py` y `salidas.py`. Como sus nombres lo indican, el primero incluirá funciones de entrada de información del usuario, y el otro salidas.

```
$ tree
├── main.py
└── reservaciones
    ├── entradas.py
    ├── __init__.py
    ├── __pycache__
    │   ├── entradas.cpython-36.pyc
    │   ├── __init__.cpython-36.pyc
    │   └── salidas.cpython-36.pyc
    └── salidas.py

$ python main.py 
Desea conocer el apartado (si/no)?si
---------------------------------------------------------------
RESERVACION                     |CANTIDAD |PRECIO   |SUBTOTAL 
Habitación doble                |        3|150000.00|450000.00
Alimentos y bebidas             |        2|  5000.00| 10000.00
Transporte                      |        2|  3000.00|  6000.00
Tour en lancha                  |        1|  2170.00|  2170.00
                                              Total |468170.00
                                           Apartado | 46817.00
```