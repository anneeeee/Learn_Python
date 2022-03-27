# 两个坛子，其中一个容量是4加仑，另一个的是3加仑。坛子上都没有刻度线。可以用水泵将它们装满水。如何使4加仑的坛子最后装有2加仑的水？
# 普通解法

# 记录不同的组合
def getLabelName(a, b):
    return 'BottleA_' + str(a) + '_BottleB_' + str(b)

# 目标水量
targetVolume = 2
findSolution = False

# 将solution存到一个栈中，以便后续找到从起始状态到目标水量的操作路径
solution = Stack()

# 使用字典保存已经尝试过的水量组合
alreadyTriedStates = {}

# 瓶子水量（可以替换为其他值）
volume_of_bottle_a = 4
volume_of_bottle_b = 3

# 对不同水量进行尝试
def trySolution(new_a, new_b):
    global findSolution
    if not alreadyTriedStates.__contains__(getLabelName(new_a, new_b)) and not findSolution:
        solution.push(getLabelName(new_a, new_b))
        findWaterSolution(new_a, new_b)
        if not findSolution:
            # new_a, new_b是无效的尝试选择，因此退出后pop掉
            solution.pop()

def findWaterSolution(a, b):
    global findSolution
    if findSolution or alreadyTriedStates.__contains__(getLabelName(a,b)):
        return
    alreadyTriedStates[getLabelName(a,b)] = 1
    if a == targetVolume:
        findSolution = True
        return
    if b == targetVolume:
        solution.push(getLabelName(0, b))
        solution.push(getLabelName(b, 0))
        findSolution = True
        return
    
    # 选择1.把a装满
    trySolution(volume_of_bottle_a, b)
    
    # 选择2. 把b装满
    trySolution(a, volume_of_bottle_b)

    # 选择3. a把b装满
    space_of_bottle_b = volume_of_bottle_b - b
    if space_of_bottle_b >= a:
        trySolution(0, a + b)
    else:
        trySolution(a - space_of_bottle_b, volume_of_bottle_b)

    # 选择4. b把a装满
    space_of_bottle_a = volume_of_bottle_a - a
    if space_of_bottle_a >= b:
        trySolution(a+b, 0)
    else:
        trySolution(volume_of_bottle_a, b - space_of_bottle_a)

    # 选择5. a清空
    trySolution(0, b)
    # 选择6. b清空
    trySolution(a, 0)

print("#############################################")
start_volume_a = 0
start_volume_b = 0
findWaterSolution(start_volume_a, start_volume_b)
print("find solution is:" + str(findSolution))
if findSolution:
    solution_str = ''
    while not solution.isEmpty():
        label = solution.pop()
        solution_str = label + '->' + solution_str
    solution_str = getLabelName(start_volume_a, start_volume_b) + '->' + solution_str + 'done'
    print(solution_str)
