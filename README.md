# Tests
Inicialmente se plantéa centrarse en las pruebas unitarias
Pero hay 3 tipos de pruebas: pruebas unitarias, pruebas de integración y pruebas del sistema(funcionales)
Luego surgen 2 postpruebas que son: Pruebas de aceptación(Validan el software que cumpla con los requerimientos por ejm del product owner) y pruebas de regresión(Luego de que se haga un cambio en el software qwue siga pasando las pruebas)
#Documentación de doctest: https://docs.python.org/3/library/doctest.html?highlight=doctest#module-doctest
#NOTA: Cuando hago los tests sin test_ ... no me los toma como tests


#Para correr los tests en archivos .txt
#Un ejemplo de lo que va dentro de estos archivos
1. This doctest checks functionality of  python's plus operator.

>>> 2 + 4
6
>>> -10.5 + 8
-2.5

2. The below doctest checks functionality of add2num function

>>> def add2num(x, y):
...       "This function returns sum of two numbers."
...       return x + y
>>> add2num(6, 7)
13
>>> add2num(-8.5, 7)
-1.5

>>> add2num(8, 'hello')
#Fin ejemplo .txt
#Finalmete lo anterior se ejecuta: python3 ‑m doctest (nombreArchivo).txt

#Para ejecutar los units tests que hay dentro de una carpeta: 
#python -m unittest discover


#ANOTHER TESTING MODULE IN PYTHON
pip install nose

#Para hacer pruebas con nose(Se debe tener en cuenta que en algunas versiones de python no funcionan algunas librerías, complementos, etc... Por ejm nosetest sirve en 3.10 pero no en 3.7.1 ó 3.7.9)
python -m nose Project2/test/test_module1.py -v


