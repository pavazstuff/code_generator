from random import randint

class Generator:
	def __init__(self):
		self.arr = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
	def cadena(self):
		str = ""
		for i in range(0, 10):
			str = str + self.arr[randint(0, len(self.arr)-1 )]
		return str
		
def something():
	x = Generator()
	while True:
		print x.cadena()
		try:
			pause = input()
		except:
			pass
	
if __name__ == "__main__":
	something()