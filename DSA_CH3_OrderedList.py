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

class OrderedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):     # 检查列表是否为空。不需要参数，返回布尔值
        return self.head == None
    def length(self):   # 返回列表中元素的个数。不需要参数，返回一个整数
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count
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

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current.getNext() != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found
    
    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
    
    def isEmpty(self):     # 检查列表是否为空。不需要参数，返回布尔值
        return self.head == None

    def length(self):   # 返回列表中元素的个数。不需要参数，返回一个整数
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

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
        return current.getData()
    
    def index(self,item): # 返回下标
        current = self.head
        pos = 0
        while current.getData() != item:
            current = current.getNext()
            pos += 1
        return pos
    
    def __str__(self):
        current = self.head
        result = ''
        while current != None:
            result = result + '→' + str(current.getData())
            current = current.getNext()
        print(result)

a = OrderedList()
a.add(1)
a.add(2)
a.add(3)
a.__str__()
print(a.isEmpty())
print(a.length())
a.remove(3)
a.__str__()
a.add(3)
a.__str__()
print(a.search(1))
print(a.search(3))
print(a.search(4))
a.add(10)
a.add(9)
a.__str__()
print(a.length())
print(a.pop())
a.__str__()
print(a.pop_pos(0))
a.__str__()
print(a.index(9))
