# 定义Node类

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data 
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data = newdata
    def setNext(self,newnext):
        self.next = newnext

# 定义UnorderedList类
class UnorderedList:
    def __init__(self):
        self.head = None   # 列表类本身并不包含任何节点对象，而只有指向整个链表结构中第一个节点的引用
    
    def isEmpty(self):     # 检查列表是否为空。不需要参数，返回布尔值
        return self.head == None
    
    def add(self,item):         # 假设item不在列表中，向其中添加item。无返回值
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def length(self):   # 返回列表中元素的个数。不需要参数，返回一个整数
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self,item): # 在列表中搜索元素item，接受一个item作为参数，返回布尔值
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self,item): # 假设元素item在列表中，从中移除item。修改列表
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:                # 开始执行删除操作，如果previous == None，说明current为头节点。
            self.head = current.getNext()   # 将头节点设置为要移除的头节点的下一个节点
        else:
            previous.setNext(current.getNext())   # 如果previous不为None，将它的后续节点设置为current节点的下一个节点

    def __str__(self):
        current = self.head
        result = ''
        while current != None:
            result = result + '→' + str(current.getData())
            current = current.getNext()
        print(result)

    
    def append(self,item): # 假设元素item之前不在列表中，并在列表最后位置添加item。无返回值
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        current.setNext(item)

    def insert(self, pos,item):  # 假设元素之前不在列表中，假设pos值合理，无返回值
        current = self.head
        current_pos = 0
        previous = None
        while current_pos != pos:
            previous = current
            current = current.getNext()
            current_pos += 1
        if previous == None:
            item.setNext(current)
            self.head = item
        else:
            item.setNext(current)
            previous.setNext(item)
            
    def pop(self): # 假设列表不为空，移除列表中的最后一个元素，并且返回它
        current = self.head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        previous.setNext(None)
        return current.getData()
        
    def pop_pos(self,pos): # 移除指定位置的元素。它接受位置参数，并且会返回一个元素
        current = self.head
        current_pos = 0
        previous = None
        while current_pos != pos:
            previous = current
            current = current.getNext()
            current_pos += 1
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())



       
a = UnorderedList()
a.add(1)
a.add(2)
a.add(3)
a.append(Node(4))
a.insert(0,Node(5))
a.insert(2,Node(6))
a.insert(6,Node(7))
print(a.pop())
print(a.pop())
a.pop_pos(0)
a.pop_pos(1)
a.pop_pos(2)
a.__str__()