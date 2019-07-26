## Reto 04

`mejor_precio.py`

De forma similar al ejemplo anterior, modifica `mejor_precio.py`, para que se pueda utilizar como módulo o como archivo independiente, su funcion de calcular mejor precio. Agrega docstrings para indicar al usuario final como utilizarlo.


```python
$ python3 mejor_precio.py 
El mejor precio es Ixtapa por $2920
$ ipython3
Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.5.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import mejor_precio

In [2]: mejor_precio?
                                        
Type:        module
String form: <module 'mejor_precio' from '/home/checor/dev/python-clases-ds/sesion03/reto04/mejor_precio.py'>
File:        ~/dev/python-clases-ds/sesion03/reto04/mejor_precio.py
Docstring:   Móudlo para mostrar el mejor precio de un array con opciones y destinos

In [3]: mejor_precio.mejor_precio?

Signature: mejor_precio.mejor_precio(destinos, tabla)
Docstring: Muestra el destino con mejor precio y su precio final
File:      ~/dev/python-clases-ds/sesion03/reto04/mejor_precio.py
Type:      function

In [4]:        

```