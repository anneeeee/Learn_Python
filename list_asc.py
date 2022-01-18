# 列表排序方法
def asc_rank(list):
    asc_list = []
    for i,val in enumerate(list):
        j = find_index(asc_list,val)
        asc_list.insert(j,val)
    return asc_list

# 找到元素插入的位置
def find_index(asc_list,num):
    j = 0
    while j < len(asc_list):
        if num > asc_list[j]:
            j = j + 1
        else:
            break
    return j

# 算法复杂度:O(n*n)

# 测试case
print(asc_rank([3,6,8,1,9,2,11,4]))
print(asc_rank([1,2,3,4,5,6,7,8]))
print(asc_rank([9,8,7,6,5,4,3,2]))