class Buffer:
	def __init__(self):
		self.currentlist = []
		# конструктор без аргументов

	def add(self, *a):
		self.currentlist = self.currentlist + list(a)
		if len(self.currentlist) < 5:
			return self.currentlist
		else:
			while len(self.currentlist) >= 5:
				suma = []
				for i in range(5):
					suma.append(self.currentlist.pop(0))
				return sum(suma)
		# добавить следующую часть последовательности

	def get_current_part(self):
		print(self.currentlist)

a = Buffer()
a.add(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
a.get_current_part()
print(a.currentlist)

