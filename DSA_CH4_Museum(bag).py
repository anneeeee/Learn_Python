# 假设一个计算机科学家兼艺术大盗闯入美术馆。他只能用一个容量为 W磅的背包来装盗取的艺术品，并且他对每一件艺术品的价值和重量了如指掌。他会如何写一个动态规划程序来帮助自己最大程度地获利呢？下面的例子可以帮助你思考：假设背包容量是20磅，艺术品为5件。

# 艺术家背包容量 20磅
W = 20
# 艺术品的重量
weight = [2,3,4,5,9]
# 艺术品对应的价值
value = [3,4,8,8,10]

# 寻找最佳解
def best_solution(W,weight,value):
    rows, cols = len(weight),W +1  # 创建dp二维数组
    dp = [[0 for _ in range(cols)] for _ in range(rows)] # 二维数组每一行每一列都填充0，得到一个5行 20列的矩阵（结果是数组里面套了5个长度为20的数组）
    dp_choice = [[0 for _ in range(cols)] for _ in range(rows)]  # 初始化一个二维数组，行为物品，列为背包重量，中间的值为是否选择该物品，如果选的话填充1，否则保持0
    
    # 初始化dp数组
    for i in range(rows):
        dp[i][0] = 0 #当背包重量为1时，无法放入任何一个艺术品，因此最大价值为0
    first_item_weight, first_item_value = weight[0], value[0]  # 拿出第一个艺术品的重量和价值
    for j in range(1,cols):  # 更新第一行的数据
        if first_item_weight <= j:  # 如果第一个物品的重量小于要遍历的背包重量，那么dp[0][j]就是第一个艺术品的价值
            dp[0][j] = first_item_value

    # 初始化dp_choice数组
    for i in range(rows):
        dp_choice[i][0] = 0  #当背包重量为1时，无法放入任何一个艺术品，因此第一行第一列填0
    first_item_weight, first_item_value = weight[0], value[0]  # 拿出第一个艺术品的重量和价值
    for j in range(1,cols):  # 更新第一行的数据
        if first_item_weight <= j:  # 如果第一个物品的重量小于要遍历的背包重量，那么dp[0][j]就是1，代表第一个物品可以放进去
            dp_choice[0][j] = 1

    # 更新dp数组：先遍历物品，再遍历背包
    for i in range(1, len(weight)):  # 依次遍历第2,3,4,5行
        cur_weight, cur_val = weight[i],value[i]  # 拿出当前物品的重量及价值
        for j in range(1, cols):  # 从第二列开始遍历（第一列初始化的时候做过了，都是0）
            if cur_weight > j:  # 说明背包装不下当前物品）
                dp[i][j] = dp[i-1][j]  # 所以不装当前物品
            else:
                # 定义dp数组：dp[i][j] 前i个物品里，放进容量为j的背包，价值总和最大是多少
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-cur_weight]+cur_val)
                if dp[i-1][j] > dp[i-1][j-cur_weight]+cur_val:
                    pass
                else:
                    dp_choice[i][j] = 1

    # print(dp)  可打印出来查看dp二维数组的结果
    # print(dp_choice)  可打印出来查看dp二维数组的结果
    max_value = dp[len(weight)-1][W]  # 取出本次行动可获得的最大收益（二维数组的最后一个值）
    print('本次行动可获得的最大收益为%s'%max_value)
    get_choices(W,len(weight),dp_choice)

# 价值最大化的前提下，列出拿了哪些物品
def get_choices(w,rows,dp_choice):
    results = []  # 构造一个数组，用于存放最佳结果由哪些艺术品组成（按艺术品编号）
    i = W  # i为当前背包重量
    j = rows - 1  # j为物品编号
    while j >= 0 :  # 遍历物品
        if dp_choice[j][i] == 1:  # 如果最后一个结果是选择
            results.append(j+1)   # 如果结果是选择，就把它加到结果的列表里面。j+1是物品的编号
            i = i - weight[j]  # 背包当前重量要减去物品j的重量
        j = j - 1  # 物品序号-1，看一下下一个物品是否放在背包内
    print('使艺术品总价值最大的艺术品编号为%s'%results)  # 打印结果


best_solution(W,weight,value)

# 备注：dp及dp_choice数组初始化也可以使用行（0~物品编号），列（0~背包重量），这样第0行（物品0代表没有）全是0，第0列（背包重量为0，无法放入物品）全是0。减少对边界的斟酌
