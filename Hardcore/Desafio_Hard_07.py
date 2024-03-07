from time import sleep

class Onibus:
	def __init__(self):
		self.velocidade = 3
		self.tempoEspera = 2
		self.EmMovimento = True
		self.estacaoAtual = 0


def main():
	onibus = Onibus()
	
	estacoes = ['Bondo', 'Primavera', 'Mendes', 'Dados', 'Queiroz']
	
	caminho = 0
	
	while onibus.EmMovimento:
		sleep(onibus.velocidade)
		
		if caminho != (len(estacoes) - 1):
			print(f'[INFO] - PARTINDO')
			sleep(onibus.tempoEspera)
			print(f'[INFO] - PARANDO NA ESTAÇÃO [{estacoes[caminho]}]')
			sleep(onibus.tempoEspera)
			caminho += 1
		else:
			print(f'[INFO] - PARANDO NA ESTAÇÃO TERMINAL [{estacoes[caminho]}]')
			onibus.EmMovimento = False
			
	
	
main()