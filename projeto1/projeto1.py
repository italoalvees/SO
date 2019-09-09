class Fila:

	class Process:
		def __init__(self, chegada, pico):
			self.chegada = chegada
			self.pico = pico
			self.resposta = 0
			self.espera = 0
			self.retorno = 0
			self.entrou = 0




	def __init__(self):
		self.ativo = None
		self.ult_round = 0
		self.process = []
		self.dentro = []
		self.terminado = []

	
	def preencher(self, lista):
		for process in lista:
			self.inserir_processo(process[0],process[1])


	def inserir_processo(self, chegada, pico):
		process = self.Process(chegada, pico)
		self.process.append(process)

		#Ordena os processos por ordem de chegada
		self.process.sort(key=lambda x: x.chegada)

	def ciclo(self):
		if self.ativo != None:
			self.ativo.pico -= 1
		
		for process in self.dentro:
			process.espera += 1

	def entrar(self, tempo):
		for p in self.process:
			if p.chegada == tempo:
				self.dentro.append(p)

	def finalizar(self, tempo):
		if self.ativo != None and self.ativo.pico == 0:
				self.ativo.retorno = tempo - self.ativo.chegada
				self.terminado.append(self.ativo)
				self.ativo = None

				if len(self.dentro):
					self.ativo = self.dentro.pop(0)
					self.ativo.resposta = tempo - self.ativo.chegada
		
		elif self.ativo == None and len(self.dentro) > 0:
				self.ativo = self.dentro.pop(0)
				self.ativo.resposta = tempo - self.ativo.chegada 		

	def sjf_sort(self):
		self.dentro.sort(key=lambda x: x.pico)

	def rr_round(self, tempo):
		if self.ativo != None and self.ativo.pico == 0:
				self.ativo.retorno = tempo - self.ativo.chegada
				self.terminado.append(self.ativo)
				self.ativo = None
				self.ult_round = tempo

				if len(self.dentro):
					self.ativo = self.dentro.pop(0)
					if self.ativo.entrou == 0 :
						self.ativo.resposta = tempo - self.ativo.chegada
						self.ativo.entrou += 1
		
		elif self.ativo == None and len(self.dentro) > 0:
				self.ativo = self.dentro.pop(0)
				if self.ativo.entrou == 0 :
						self.ativo.resposta = tempo - self.ativo.chegada
						self.ativo.entrou += 1
		elif self.ativo != None and tempo - self.ult_round == 2:
				self.dentro.append(self.ativo)
				self.ativo = self.dentro.pop(0)
				self.ult_round = tempo
				if self.ativo.entrou == 0:
					self.ativo.resposta = tempo - self.ativo.chegada
					self.ativo.entrou += 1




def FCFS(lista):
	
	fila = Fila()

	fila.preencher(lista)
	fim = len(fila.process)

	tempo = 0	

	while(len(fila.terminado) < fim) :
		
		fila.entrar(tempo)
		fila.finalizar(tempo)
		fila.ciclo()
		tempo += 1
		

	retorno = 0
	resposta = 0
	espera = 0	

	for process in fila.terminado:
		retorno += process.retorno
		resposta += process.resposta
		espera += process.espera

	print("FCFS", str(round(retorno/len(fila.terminado),1)).replace('.',','), str(round(resposta/len(fila.terminado),1)).replace('.',','), str(round(espera/len(fila.terminado),1)).replace('.',','))


def SJF(lista):
	
	fila = Fila()

	fila.preencher(lista)
	fim = len(fila.process)

	tempo = 0	

	while(len(fila.terminado) < fim) :
		fila.entrar(tempo)
		fila.sjf_sort()
		fila.finalizar(tempo)
		fila.ciclo()
		tempo += 1
		

	retorno = 0
	resposta = 0
	espera = 0	

	for process in fila.terminado:
		retorno += process.retorno
		resposta += process.resposta
		espera += process.espera

	print("SJF", str(round(retorno/len(fila.terminado),1)).replace('.',','), str(round(resposta/len(fila.terminado),1)).replace('.',','), str(round(espera/len(fila.terminado),1)).replace('.',','))

def RR(lista):
	
	fila = Fila()

	fila.preencher(lista)
	fim = len(fila.process)



	tempo = 0	

	while(len(fila.terminado) < fim) :
		fila.entrar(tempo)
		fila.rr_round(tempo)
		fila.ciclo()
		tempo += 1
		


	retorno = 0
	resposta = 0
	espera = 0	

	for process in fila.terminado:
		retorno += process.retorno
		resposta += process.resposta
		espera += process.espera

	print("RR", str(round(retorno/len(fila.terminado),1)).replace('.',','), str(round(resposta/len(fila.terminado),1)).replace('.',','), str(round(espera/len(fila.terminado),1)).replace('.',','))





def get_process(filename):

    values = []
    lista = []

    with open(filename, 'r') as r:
        for line in r:
            line = line.replace('\t', ' ')
            line = line.replace('\n', ' ')
            for i in line.split(' '):
                if i != '':
                    values.append(int(i))

    for x in range(0, len(values), 2):
    	lista.append((values[x],values[x+1]))


    return lista



lista = get_process("process.txt")


FCFS(lista)
SJF(lista)
RR(lista)


	






		