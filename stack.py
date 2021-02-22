class Stack:
	def __init__(self):
		self.array=[]
		self.top=-1
	def push(self,val):
		self.array.append(val)
		self.top+=1
	def pop(self):
		val=self.array.pop(self.top)
		self.top-=1
		return val
	def peek(self):
		return(self.array[self.top])
	def display(self):
		for i in self.array:
			print(i,end=" ")
		print("")
	def get_len(self):
		return(len(self.array))

stack=Stack()
stack.push(10)
stack.display()
stack.push(20)
stack.display()
stack.push(30)
stack.display()
stack.push(40)
stack.display()
stack.push(50)
stack.display()
v=stack.pop()
print(v)
stack.display()
v=stack.pop()
print(v)
stack.display()
v=stack.peek()
print(v)
stack.display()

