class Buffer:
	def __init__(self):
		self.currentlist = []
		# конструктор без аргументов

	def add(self, *a):
		self.currentlist = self.currentlist + list(a)
		if len(self.currentlist) < 5:
			return self.currentlist
		else:
			suma = []
			for i in range(5):
				elem = self.currentlist.pop(0)
				suma.append(elem)
			return sum(suma)
		# добавить следующую часть последовательности

	def get_current_part(self):
		pass 
a = Buffer()
a.add(1,2,3,4,5,6)
print(a.currentlist)

