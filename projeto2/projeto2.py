class Fifo:

	def __init__(self, n_quadros, lista):
		self.buf = [None]*n_quadros
		self.falta = 0
		self.lista = lista

	def entrar(self, valor):
		entrou = False
		for i in range(len(self.buf)):
			if(self.buf[i] == valor):
				entrou = True
				return 0
			elif(self.buf[i] == None):
				self.buf[i] = valor
				self.falta +=1
				entrou = True
				return 0
		if(not entrou):
			self.falta += 1
			self.buf.pop(0)
			self.buf.append(valor)
				

	def run(self):
		for i in self.lista:
			self.entrar(i)

		print("FIFO",self.falta)

class Otimo:

	def __init__(self, n_quadros, lista):
		self.buf = [None]*n_quadros
		self.dist = [0]*n_quadros
		self.falta = 0
		self.lista = lista


	def distancia(self,atual):
		for i in range(len(self.buf)):
			self.dist[i] = 0
			for j in range(atual, len(self.lista)):
				if(self.buf[i] == self.lista[j]):
					self.dist[i] = j - atual
					break
				elif(j == len(self.lista)-1):
					self.dist[i] = -1



	def entrar(self, valor, atual):
		entrou = False
		ja = False
		indice = -1
		maior = -1


		self.distancia(atual)

		for i in range(len(self.buf)):
			
			if(self.dist[i] > maior and not ja):
				maior = self.dist[i]
				indice = i
			elif(self.dist[i] == -1):
				ja = True
				indice = i

			if(self.buf[i] == valor):
				entrou = True
				return 0
			elif(self.buf[i] == None):
				self.buf[i] = valor
				self.falta +=1
				entrou = True
				return 0
		if(not entrou):
			if(atual == len(self.lista)-2):
				self.falta += 1
				self.buf.pop(0)
				self.buf.append(valor)
			else:
				self.falta += 1
				self.buf.pop(indice)
				self.buf.append(valor)
				

	def run(self):
		for i in range(len(self.lista)):
			self.entrar(self.lista[i],i)

		print("OTM",self.falta)


class LRU:

	def __init__(self, n_quadros, lista):
		self.buf = [None]*n_quadros
		self.falta = 0
		self.lista = lista

	def entrar(self, valor):
		entrou = False
		for i in range(len(self.buf)):
			if(self.buf[i] == valor):
				self.buf.pop(i)
				self.buf.append(valor)
				entrou = True
				return 0
			elif(self.buf[i] == None):
				self.buf[i] = valor
				self.falta +=1
				entrou = True
				return 0
		
		if(not entrou):
			self.falta += 1
			self.buf.pop(0)
			self.buf.append(valor)
				

	def run(self):
		for i in self.lista:
			self.entrar(i)
			
		print("LRU",self.falta)

def get_values(filename):

    values = []

    with open(filename, 'r') as r:
        for line in r:
            line = line.replace('\t', ' ')
            line = line.replace('\n', ' ')
            for i in line.split(' '):
                if i != '':
                    values.append(int(i))

    return values

lista = get_values('entrada.txt')
quadro = lista.pop(0)

print(lista)
 
f = Fifo(quadro,lista)
f.run()

o = Otimo(quadro,lista)
o.run()

l = LRU(quadro,lista)
l.run()

