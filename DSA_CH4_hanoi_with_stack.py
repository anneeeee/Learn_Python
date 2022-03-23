# 汉诺塔，用3个栈记录盘子的位置

fromStack = Stack()
withPole = Stack()
toPole = Stack()
def hanoiWithStack(height,fromPole,withPole,toPole):
    if height == 1:
        toPole.push(height)
        print('将盘子%s移到%s' % (height,toPole))
    else:
        hanoiWithStack(height-1,fromPole,toPole,withPole)
        toPole.push(height)
        print('将盘子%s移到%s' % (height,toPole))
        hanoiWithStack(height-1,withPole,fromPole,toPole)

hanoiWithStack(3,fromStack,withPole,toPole)
