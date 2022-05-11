from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

gui = Usuario ('Gui')
miguel = Usuario ('Miguel')

lance_do_gui = Lance(gui, 150.0)
lance_do_miguel =Lance(miguel, 100.0)

leilao = Leilao('Carro')

leilao.lances.append(lance_do_miguel)
leilao.lances.append(lance_do_gui)

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}')
