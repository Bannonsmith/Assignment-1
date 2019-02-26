class Stack:
    def __init__(self):
        self.dishes = []


    def push(self,value):
        self.dishes.append(value)
        print(self.dishes)

    def poop(self):
        self.dishes.pop()
        print(self.dishes)

stack = Stack()
print(stack.dishes)
stack.push('pbj')
stack.push('pbj')
stack.push('pbj')
stack.push('pbj')
stack.push('kkkkkkk')
stack.poop()
# print(stack1)
# print(stack1.dishes)
