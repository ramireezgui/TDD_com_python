from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):
    
    def test_avalia(self):
        gui = Usuario('Gui')
        miguel = Usuario('Miguel')

        lance_do_gui = Lance(gui, 150.0)
        lance_do_miguel = Lance(miguel, 100.0)

        leilao = Leilao('Carro')

        leilao.lances.append(lance_do_miguel)
        leilao.lances.append(lance_do_gui)

        avaliador = Avaliador ()
        avaliador.avalia(leilao)

        menor_valor_esperado: 100.0
        maior_valor_esperado: 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)