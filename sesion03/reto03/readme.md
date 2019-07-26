## Reto 03

`mejor_precio.py`

Un usuario está comparando precios en Bedu Travels para elegir un destino. Ha seleccionado paquetes con diferentes opciones, y desea decidirse por el mejor precio. La selección del usuario está formada de la siguiente manera, en un array de numpy. Muestre al usuario la mejor opción en cuanto a precio.

![](valores.png)

Los costos totales deberán calcularse recorriendo por columna. Se recibirán 3 parámetros:
1. Lista de amenidades
2. Lista de destinos
3. Array de numpy con amenidades/destinos

Definidos de la siguiente manera:
```python
destinos = ["Ixtapa", "Acapulco", "Cancún"]
opciones = ["Hospedaje", "Transporte", "Excursion", "Comida"]

valores = np.array([[1500, 3000, 4500], 
                    [800, 1200, 100], 
                    [500, 800, 1200], 
                    [ 120, 240, 360]])
```
Para obtener el siguiente resultado:
```
$ python mejor_precio.py

El mejor precio es Ixtapa por $2920

```