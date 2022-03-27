# 题目：两个坛子，其中一个容量是4加仑，另一个的是3加仑。坛子上都没有刻度线。可以用水泵将它们装满水。如何使4加仑的坛子最后装有2加仑的水？

# 定义一个栈类
class Stack:
    '''栈类.

    定义一个栈，用于提供反转特性

    属性：
        items:栈中的内容
    '''
    def __init__(self): # 创建一个栈
        self.items = []

    def is_empty(self):  # 检查栈是否为空
        return self.items == []
    
    def push(self,item): # 向栈中添加一个元素
        self.items.append(item)
    
    def pop(self): # 弹出栈顶的元素
        return self.items.pop()
    
    def peek(self): # 返回栈顶的元素（但该元素不移出栈）
        return self.items[len(self.items)-1]

    def size(self): # 返回栈的大小
        return len(self.items)

    def clear(self):  # 清空栈
        self.items = []

    def get_all_items(self):  # 按先进后出的顺序，列出栈中的所有值
        result = ''
        for i in self.items:
            result = result + str(i) + '→'
        return result

# 使用get_label_name方法，当尝试瓶子中不同的水量时，进行记录，并且始终保持A瓶子的水量在前，B瓶子的水量在后
def get_label_name(a, b):
    return 'BottleA_' + str(a) + '_BottleB_' + str(b)

TARGET_VOLUME = 2  # 使用TARGET_VOLUME全局常量保存最终求解的目标值
find_solution = False  # 使用find_solution全局变量标识当前是否找到解，用于判断函数是否执行
solution = Stack() # 使用solution全局变量，记录瓶子之间倒水的路径，等最终确认解决方案后，打印出倒水的方法

# 定义一个全局变量state_in_stack字典，在路径搜索中，如果当前路径没有返回（找到倒水的方法），不能走回头路
# 否则会死循环
state_in_stack = {}  

solutions = {}  # 定义一个全局变量字典，用于存放所有可能的倒水方法
VOLUME_OF_BOTTLE_A = 4  # 定义一个全局常量，用于存放题目中较大的瓶子容量
VOLUME_OF_BOTTLE_B = 3  # 定义一个全局常量，用于存放题目中较小的瓶子容量

# 尝试不同的倒水方法
# 如果该路径上没有尝试过new_a, new_b这种水量组合
# 把此种方法压入solution栈中，以便后续回溯方法的时候能找到这种组合
# 使用新的水量进行尝试
# 尝试完毕后，返回上一层，同时删除无效的尝试
def try_solution(new_a, new_b):
    global find_solution
    if not state_in_stack.__contains__(get_label_name(new_a,new_b)):
        solution.push(get_label_name(new_a, new_b))
        findWaterSolution(new_a, new_b)
        solution.pop()
        del state_in_stack[get_label_name(new_a,new_b)]

# 保存所有可能的解
# 如果找到了一种可能的解
# 通过分析solution栈的大小了解此种解法的复杂度
# 将solution栈转换为字符串
# 以solution字符串为key，solution对应的复杂度为value，存入solutions字典，以便后续在字典中找到最优解
def save_solution(solution):
    if find_solution:
        complexity = solution.size()
        solution_str = solution.get_all_items()
        solution_str = solution_str + 'done'
        solutions[solution_str] = complexity

# 找到倒水的方法
# 如果此种方法之前在该条路径尝试过（未达到find_solution状态下，不用再走回头路，否则会死循环），就退出当前函数
# 把现在尝试的方法记录到state_in_stack中，一方面不走回头路，另一方面便于后续回溯解题方法
# 如果a中的水量等于目标水量TARGET_VOLUME，则代表找到了一种解法，并把这种方法记录到solutions中
# 否则，依次尝试不同的水量，包括6种选择（把a装满，b为空；a为空，把b装满；将a的水倒入b；将b的水倒入a；把a清空；把b清空）
def findWaterSolution(a, b):
    global find_solution
    global solution
    if state_in_stack.__contains__(get_label_name(a,b)):
        return
    state_in_stack[get_label_name(a,b)] = 1
    if a == TARGET_VOLUME:
        find_solution = True
        save_solution(solution)
        return
    
    # 选择1. 把a装满
    try_solution(VOLUME_OF_BOTTLE_A, b)
    
    # 选择2. 把b装满
    try_solution(a, VOLUME_OF_BOTTLE_B)

    # 选择3. a把b装满
    space_of_bottle_b = VOLUME_OF_BOTTLE_B - b
    if space_of_bottle_b >= a:
        try_solution(0, a + b)
    else:
        try_solution(a - space_of_bottle_b, VOLUME_OF_BOTTLE_B)

    # 选择4. b把a装满
    space_of_bottle_a = VOLUME_OF_BOTTLE_A - a
    if space_of_bottle_a >= b:
        try_solution(a+b, 0)
    else:
        try_solution(VOLUME_OF_BOTTLE_A, b - space_of_bottle_a)

    # 选择5. a清空
    try_solution(0, b)

    # 选择6. b清空
    try_solution(a, 0)

print("----------------------------------")
start_volume_a = 0  # 瓶子A的容量从0开始
start_volume_b = 0  # 瓶子B的容量从0开始
findWaterSolution(start_volume_a, start_volume_b)  # 调用findWaterSolution函数进行求解
print("find solution is:" + str(find_solution))  # 打印是否找到解决方案

# 将每种解决方案的复杂度放入列表中，找到最小值。最小值对应的key为最佳解决方案
all_solution_complexity = solutions.values()
best_solution_complexity = min(all_solution_complexity)

def get_best_result(dict,value):
    return [k for k, v in dict.items() if v==value]

print('------------打出所有解------------')
print(solutions)
print('----------------------------------')
print(get_best_result(solutions,best_solution_complexity))
print('经过%s步完成' % best_solution_complexity)
