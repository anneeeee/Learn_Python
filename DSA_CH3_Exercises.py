# 定义一个栈类
class Stack:
    def __init__(self): #创建一个栈
        self.items = []

    def isEmpty(self):  #检查栈是否为空
        return self.items == []
    
    def push(self,item): #向栈中添加一个元素
        self.items.append(item)
    
    def pop(self): #弹出栈顶的元素
        return self.items.pop()
    
    def peek(self): #返回栈顶的元素（但该元素不移出栈）
        return self.items[len(self.items)-1]

    def size(self): #返回栈的大小
        return len(self.items)

# 讨论题，十进制数转二进制数
def decimalToBinary(num):
    stack = Stack()
    quotient = 1
    divider = 2
    while num/divider >0:
        quotient = num//divider
        remainder = num%divider
        stack.push(remainder)
        num = quotient
    result = ''
    while stack.isEmpty() == False:
        result = result + str(stack.pop())
    return result

a = decimalToBinary(96)
print(a)
         