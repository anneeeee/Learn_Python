#链表

# 定义Node类

class Node():
    def __init__(self, initdata, next = None, pre = None):
        self.data = initdata
        self.next = next
        self.pre = pre
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def getPre(self):
        return self.pre
    def setData(self, newdata):
        self.data = newdata
    def setNext(self, newnext):
        self.next = newnext
    def setPre(self, newpre):
        self.pre = newpre
    def __str__(self):
        return self.getData()
    # 建议定义一个内部函数，输入的是Node，返回的是反转后新链表的头部
    def node_reverse(node):
        nNode = node.getNext()
        newNode = nNode.append(node)
        node.setNext(None)

# 返回值：[new_head, tail], new_head是反转后的链表头部结点，tail是反转后的链表的尾部节点
def inner_reverse(head: Node):
    # 如果当前节点是None或者没有后继节点，则说明不需要反转，直接返回
    if head == None or head.getNext() == None:
        head.setPre(None)
        head.setNext(None)
        return [head, head]
    # 取出头节点, 对后继节点进行反转得到result，result[0]是后继节点反转后的头节点，result[1]是尾节点
    result = inner_reverse(head.getNext())
    head.setPre(result[1])
    head.setNext(None)
    result[1].setNext(head)
    return [result[0], head]

# 定义UnorderedList类
class UnorderedList():
    # head, tail均是Node实例
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
    # 检查链表是否为空
    def isEmpty(self):
        return self.head == None
    # item是一个Node实例
    def add(self,item):
        if self.head == None:
            self.head = item
            self.tail = item
        else:
            item.setPre(self.tail)
            self.tail.setNext(item)
            self.tail = item
    def __str__(self):
        result = 'head.value=' + str(self.head.getData()) + ', tail.value=' + str(self.tail.getData()) + ', list:'
        curNode = self.head
        while curNode != None:
            result += str(curNode.getData()) + '->'
            curNode = curNode.getNext()
        result += 'None'
        return result
    # 反转打印链表
    def reverse_str(self):
        result = 'head.value=' + str(self.head.getData()) + ', tail.value=' + str(self.tail.getData()) + ', reverse:'
        curNode = self.tail
        while curNode != None:
            result += str(curNode.getData()) + '->'
            curNode = curNode.getPre()
        result += 'None'
        return result
    # 实现链表的反转--方法一
    def reverse(self):
        curNode = self.head
        pNode = None
        while curNode != None:
            nNode = curNode.getNext()
            curNode.setNext(pNode)
            pNode = curNode
            curNode = nNode
        self.tail = self.head
        self.head = pNode
        return self

    # 实现链表的反转--方法二
    def recursive_reverse(self):
        newLink = UnorderedList()
        def getRemainLink(item):
            remainLink = UnorderedList(head = item, tail= self.tail)
            popItem = item
            newLink.append(popItem)
        if self.length() == 1:
            return self
        else:
            curNode = self.head
            while curNode.getNext() != None:
                getRemainLink(curNode.getNext())
                curNode = curNode.getNext()
            return self
   
    # 实现链表的反转 -- 递归方法
    def reverse_by_recursion(self):
        result = inner_reverse(self.head)
        self.head = result[0]
        self.tail = result[1]
        
    # 返回链表的长度
    def length(self):
        curNode = self.head
        count = 1
        while curNode.getNext() != None:
            count += 1
            curNode = curNode.getNext()
        return count

    # 删除链表中的元素
    def remove(self,item):
        # 假设curNode是链表的头部，便于从头部开始遍历链表
        curNode = self.head
        # 设置一个counter计算共删除了几个元素
        find = 0
        # 先查看链表的长度
        if self.length() == 1:
            # 如果链表长度为1，且数据等于需要删除的内容，则链表头设为None，find+1
            if curNode.getData() == item:
                self.head == None
                find += 1
        # 如果链表长度 > 1
        else:
            # 如果curNode不为空，则进行以下循环
            while curNode != None:
                # 如果curNode的值等于待删除的值
                if curNode.getData() == item:
                    # 如果curNode是链表的头部，则把链表头部设为当前节点的下一个节点，并且下一个节点的pre要设置为none
                    if curNode.getPre() == None:
                        self.head = curNode.getNext()
                        curNode.getNext().setPre(None)
                    # 如果curNode是链表的尾部，则把链表尾部设置为当前节点的前一个节点，并且前一个节点的next要设置为none
                    elif curNode.getNext() == None:
                        self.tail = curNode.getPre()
                        curNode.getPre().setNext(None)
                    # 如果curNode在链表中间，则把当前节点的上一个节点的下一个节点设置为当前节点的下一个节点 \
                    # 把当前节点下一个节点的前一个节点设置为当前节点的前一个节点 \
                    # 设置完毕后，把当前节点的pre和next都设置为None
                    else:
                        curNode.getPre().setNext(curNode.getNext())
                        curNode.getNext().setPre(curNode.getPre())
                        curNode.setPre(None)
                        curNode.setNext(None)
                    # 找到后，counter+1
                    find += 1
                # 将curNode移到下一个节点，以便再次比较是否和所需删除的值一致
                curNode = curNode.getNext()
        # 如果find等于0，则说明链表中不存在该元素，否则返回共删除了几个值，删除了哪些
        if find == 0:
            print("链表中不存在该元素")
        else:
            print(f'删除了{find}个元素,删除的值为{item}')
        return self

    #搜索链表中的元素
    def search(self,item):
        curNode = self.head
        find = 0
        while curNode != None:
            if curNode.getData() == item:
                find += 1
            else:
                print('链表中不存在该元素')
            curNode = curNode.getNext()
        print(f'链表中共找到{find}个{item}')
    
    # 链表的追加
    def append(self,item):
        if self.head == None:
            self.head = item
            self.tail = item
        else:
            item.setPre(self.tail)
            self.tail.setNext(item)
            self.tail = item
    
    # 返回链表中某个元素的下标
    def index(self,item):
        curNode = self.head
        find = 0
        index = 0
        if curNode == None:
            print('链表为空')
        else:
            while curNode != None:
                if curNode.getData() == item:
                    print(f'元素{item}在链表中的下标为{index}')      
                    find +=1
                curNode = curNode.getNext()
                index += 1
        if find == 0:
            print(f'该链表中没有{item}')
    
    # 向链表中的指定位置插入值
    def insert(self,pos,item):
        val = item.__str__()
        print(f'在链表的位置{pos}插入值{val}')
        curNode = self.head
        i = 0
        max_index = self.length()
        while i < pos < max_index:
            curNode = curNode.getNext()
            i += 1      
        if pos == 0:
            self.head.setPre(item)
            item.setNext(self.head)
            self.head = item
        elif pos == max_index:
            self.tail.setNext(item)
            item.setPre(self.tail)
            self.tail = item
        elif 0 < pos < max_index:
            curNode.getPre().setNext(item)
            item.setPre(curNode.getPre())
            item.setNext(curNode)
            curNode.setPre(item)
        else:
            raise RuntimeError('输入位置非法')

    # 定义链表的pop方法，移除链表的最后一个元素，并返回该值
    def pop(self):
        curNode = self.tail
        if self.length == 0:
            raise RuntimeError('链表长度为0，无法使用pop方法')
        else:
            self.tail = curNode.getPre()
            curNode.getPre().setNext(None)
            curNode.setPre(None)
            return curNode
    
    # 删除链表指定位置的值
    def pop(self,pos):
        print(f'删除链表位置{pos}的值')
        curNode = self.head
        i = 0
        max_index = self.length()
        while i < pos < max_index:
            curNode = curNode.getNext()
            i += 1      
        if pos == 0:
            self.head = curNode.getNext()
            curNode.getNext().setPre(None)
            curNode.setNext(None)
        elif 0 < pos < max_index:
            curNode.getPre().setNext(curNode.getNext())
            curNode.getNext().setPre(curNode.getPre())
            curNode.setPre(None)
            curNode.setNext(None)
        else:
            print('输入位置非法')
            
            


a = UnorderedList()
print("创建一个链表")
a.add(Node(10))
a.add(Node(11))
a.add(Node(12))
a.add(Node(13))
print(a)
# print(a.reverse_str())
# print(a.length())
# a.remove(10)  
# print(a)
# print(a.reverse_str())
# print(a.length())
# a.remove(12)
# print(a)
# print(a.reverse_str())
# print(a.length())
# a.remove(13)
# print(a)
# print(a.reverse_str())
# print(a.length())
print(a)
a.insert(0,Node(9))
print(a)
print(a.reverse_str())
a.insert(5,Node(15))
print(a)
print(a.reverse_str())
a.insert(5,Node(14))
# print(a)
# print(a.reverse_str())
# a.pop()
# print(a)
# a.pop()
# print(a)
a.pop(0)
print(a)
print(a.reverse_str())
a.pop(6)
print(a)
print(a.reverse_str())
a.pop(3)
print(a)
# print(a.reverse_str())
# print(a.reverse())
# print(a.recursive_reverse())
a.reverse_by_recursion()
print(a)
print(a.reverse_str())

