
"""
1.顺序表存储（典型的数组）
     原理：顺序表存储是将数据元素放到一块连续的内存存储空间，相邻数据元素的存放地址也相邻（逻辑与物理统一）。
     优点：（1）空间利用率高。（局部性原理，连续存放，命中率高）
          （2）存取速度高效，通过下标来直接存储。

     缺点：（1）插入和删除比较慢，比如：插入或者删除一个元素时，整个表需要遍历移动元素来重新排一次顺序。
          （2）不可以增长长度，有空间限制,当需要存取的元素个数可能多于顺序表的元素个数时,会出现"溢出"问题.当元素个数远少于预先分配的空间时,空间浪费巨大。
     时间性能 :查找 O(1) ,插入和删除O（n）。
2.链表存储
    原理：链表存储是在程序运行过程中动态的分配空间，只要存储器还有空间，就不会发生存储溢出问题，相邻数据元素可随意存放，但所占存储空间分两部分，一部分存放结点值，另一部分存放表示结点关系间的指针。
    优点：（1）存取某个元素速度慢。
         （2）插入和删除速度快，保留原有的物理顺序，比如：插入或者删除一个元素时，只需要改变指针指向即可。
         （3）没有空间限制,存储元素的个数无上限,基本只与内存空间大小有关.

    缺点：（1）占用额外的空间以存储指针(浪费空间，不连续存放，malloc开辟，空间碎片多)
         （2）查找速度慢，因为查找时，需要循环链表访问，需要从开始节点一个一个节点去查找元素访问。
    时间性能 :查找 O(n) ,插入和删除O（1）。
*频繁的查找却很少的插入和删除操作可以用顺序表存储，堆排序,二分查找适宜用顺序表.
*如果频繁的插入和删除操作很少的查询就可以使用链表存储
*顺序表适宜于做查找这样的静态操作；链表适宜于做插入、删除这样的动态操作。
*若线性表长度变化不大，如果事先知道线性表的大致长度，比如一年12月，一周就是星期一至星期日共七天，且其主要操作是查找，则采用顺序表；若线性表长度变化较大或根本不知道多大时，且其主要操作是插入、删除，则采用链表，这样可以不需要考虑存储空间的大小问题。
*顺序表:顺序存储，随机读取
链式:随机存储,顺序读取(必须遍历)

"""

# Python实现链表的方式

'''
单链表的基本操作：
 1、验证链表里面有没有值！
 2、从头部插入数值！
 3、从尾部插入数值！
 4、按指定位置插入数值！
 5、删除操作！
 6、查找一个节点是否在链表中！
 7、按下标查找节点处的数值！
 8、给链表排序！
 9、修改！
'''


# 创建节点
class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


# 创建单链表
class SingleLinkedList(object):

    # 定义初始链表头部为None，长度为0
    def __init__(self):
        self.header = None
        self.length = 0

    # 判断链表是否为空
    def is_empty(self):
        if self.header is None:
            return True
        else:
            return False

    # 头部添加节点
    def add(self, node):
        if self.header.is_empty():
            self.header = node
        else:
            node.next = self.header
            self.header = node
            self.length += 1

    # 在尾部添加节点
    def append(self, node):
        current_node = self.header
        if self.is_empty():
            self.add(node)
        else:
            while current_node is not None:
                current_node = current_node.next
            current_node.next = node
            self.length += 1

    # 添加索引
    def insert(self, index, node):
        current_node = self.header
        
        if index > self.length+1 or index <= 0:
            while index > self.length+1 or index <= 0:
                print('插入索引位置有误')
                index = int(input('请重新输入插入索引'))
        elif index == 1:
            self.add(node)
        elif index == 2:
            # 把头结点指针的None交给第二节点,在最后一个节点的指针指向的是None
            node.next = self.header.next
            self.header.next = node
            self.length += 1
        # 先遍历索引之前的所有节点
        else:
            for i in range(1, index-1):
                current_node = current_node.next
            node.next = current_node.next
            current_node.next = node
            self.length += 1

    # 遍历链表中的数据
    def travel(self):
        current_node = self.header
        if self.length == 0:
            print('目前链表中没有数据')
        else:
            print('链表中有元素', end='')
            for i in range(1, self.length):
                print('s' % current_node.data, end='')
                current_node = current_node.next
            print('\n')

    # 按索引删除节点
    def delete_index(self, index):
        if index > self.length or index <= 0:
            while index > self.length or index <= 0:
                print('删除的下标不对，请重新输入下标')
                index = int('请输入新的下标')
        elif index == 1:
            self.header = self.header.next
            currentNode = self.header
        elif index == 2:
            current_node = self.header
            current_node.next = current_node.next.next
        else:
            current_node = self.header
            for i in range(1, index - 1):
                current_node = current_node.next
            current_node.next = current_node.next.next
            self.length += 1



















if __name__ == '__main__':

    pass





































