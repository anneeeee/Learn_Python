#计算后续表达式
'''
1. 输入一个后序表达式
2. 依次读后序表达式中的值
3. 如果读取的结果是数字，则压入栈
4. 如果读取的结果是操作符，则拿出栈中最近的两个数做操作，操作后压回栈中
5. 表达式遍历结束后，检查栈的大小是否为1，如果等于1，返回结果，否则报错提示检查输入是否合法
'''



# 定义一个栈类，执行各类运算
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

cal_exp = input('请输入一个后缀表达式：')

def suffix_calculation(user_input):
    num_stack = Stack()
    for i in cal_exp:
        if i>= '0' and i <= '9':
            num_stack.push(int(i))
        elif i in ['+','-','*','/']:
            num2 = num_stack.pop()
            num1 = num_stack.pop()
            newnum = do_math(num1,i,num2)
            num_stack.push(newnum)
    if num_stack.size() == 1:
        return num_stack.peek()
    else:
        raise RuntimeError('非法表达式，请重新输入')

def do_math(op1,fuhao,op2):
    if fuhao == '+':
        return op1 + op2
    elif fuhao == '-':
        return op1 - op2
    elif fuhao == '*':
        return op1 * op2
    elif fuhao == '/':
        return op1 / op2
    else:
        raise RuntimeError('无法支持该操作符：'+fuhao)

print(suffix_calculation(cal_exp))