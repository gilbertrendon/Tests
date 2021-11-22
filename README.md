# Tests
Inicialmente se plantéa centrarse en las pruebas unitarias
Pero hay 3 tipos de pruebas: pruebas unitarias, pruebas de integración y pruebas del sistema(funcionales)
Luego surgen 2 postpruebas que son: Pruebas de aceptación(Validan el software que cumpla con los requerimientos por ejm del product owner) y pruebas de regresión(Luego de que se haga un cambio en el software qwue siga pasando las pruebas)
#Documentación de doctest: https://docs.python.org/3/library/doctest.html?highlight=doctest#module-doctest



from sample_module import sample_tests
add2num = sample_tests.add2num()

# def add2num(x, y):
#      return x + y

import unittest

class Testadd2num(unittest.TestCase):

    def test_sum_2pos_num(self):
      self.assertEqual(add2num(6, 7), 13)

    def test_sum_1pos_and_1neg_num(self):
      self.assertEqual(add2num(-10, 9), -1)

