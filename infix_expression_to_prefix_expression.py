# 将中序表达式转换为前序表达式

'''
举例：
中序表达式：A*B+C*D
前序表达式：+*AB*CD
计算步骤：
1. 用户输入一个中序表达式
2. 遍历中序表达式的每一个字符
3. 如果遇到字母，把它压入字母栈中
4. 如果遇到'('，压入符号栈中
5. 如果遇到计算符号(包括'+'、'-'、'*'、'/')：
   如果符号栈为空，把计算符号压入fuhao_stack中，\
   如果遇到)，当栈不为空且栈顶元素不为'('时，需要pop 符号栈中的元素并进行计算直到遇到(
   当遇到+-*/计算符时，需要和栈内的计算符比较一下优先级。如果优先级＞栈内的运算符，则把运算符压到栈中 \
   如果栈内的运算符的优先级≥未入栈运算符，则先拿出zimu_stack中的两个字母，fuhao_stack栈内的运算符，生成一个字符串，把这个运算符压回到栈内
6. 重复上述过程直到遍历完成
7. 检查zimu_stack和fuhao_stack是否为空，如果均为空，返回前序表达式字符串，如果有任一不为空，报错提示输入不合法
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

# 定义四则运算符号的优先级
fuhao_youxianji = {'+':1,'-':1,'*':2,'/':2}

# 接收用户输入
user_input = input('请输入一个计算公式：')

# 定义一个中缀表达式转前缀表达式的函数
def middle_to_front(input_str):
    #新建两个栈，一个用于存放表达式中的字母，一个用于存放表达式中的符号
    zimu_stack = Stack()
    fuhao_stack = Stack()
    #遍历input
    for i in input_str:
        if i.isalpha() == True:
            zimu_stack.push(i)  # 如果i是字母，压入字母栈
        elif i == '(':          # 如果i是左括号，压入符号栈
            fuhao_stack.push(i)
        elif i == ')':          
            while fuhao_stack.isEmpty() != True and fuhao_stack.peek() != '(':  #如果i是右括号，检查栈不为空且栈顶不为(时，反复执行计算，并将结果压入字母栈
                exp_reverse(zimu_stack,fuhao_stack)
            if fuhao_stack.peek() == '(': # 直到遇到(时，将(移出栈
                fuhao_stack.pop()
            else:
                raise RuntimeError('括号不匹配，输入的表达式非法！')
        elif i in ['+','-','*','/']:
            while fuhao_stack.isEmpty() != True \
                and fuhao_stack.peek() != '(' \
                and fuhao_youxianji[fuhao_stack.peek()] >= fuhao_youxianji[i] :  #如果i是符号，检查和栈内已有符号的优先级，如果优先级比栈内已有符号高，则压入栈。如果优先级≤栈内已有符号，则需要等栈内优先级较高的运算符号先执行运算
                exp_reverse(zimu_stack,fuhao_stack)
            fuhao_stack.push(i)
        else:
            raise RuntimeError('输入的表达式中含有非法字符:'+i)
    while fuhao_stack.isEmpty() == False:
        exp_reverse(zimu_stack,fuhao_stack)
    return zimu_stack.peek()

# 定义一个计算局部结果的函数
def exp_reverse(stack1,stack2): # stack1表示字母栈，stack2表示符号栈
    exp_i = stack2.pop()  # 从运算符栈中拿出一个值作为运算符
    try:
        a = stack1.pop() # 从字母栈中拿出第一个值
        b = stack1.pop() # 从字母栈中拿出第二个值
        c = [] # 创建一个空的列表，用于写出该部分表达式的结果
        c.insert(0,a)
        c.insert(0,b)
        c.insert(0,exp_i)
        stack1.push(''.join(c))
    except:
        raise RuntimeError("输入的表达式非法！")
    
# 返回转换结果
print(middle_to_front(user_input))