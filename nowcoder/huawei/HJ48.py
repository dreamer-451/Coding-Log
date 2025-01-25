"""
HJ37 统计每个月兔子的总数

功能:
输入一个单向链表和一个节点的值，从单向链表中删除等于该值的节点，删除后如果链表中无节点则返回空指针。
链表的值不能重复。

数据范围：
链表长度满足 1 ≤ n ≤ 1000
节点中的值满足 0 ≤ val ≤ 10000
测试用例保证输入合法

输入：
输入一行，有以下4个部分：
1 输入链表结点个数
2 输入头结点的值
3 按照格式插入各个结点
4 输入要删除的结点的值

输出：
输出一行
输出删除结点后的序列，每个数后都要加空格

示例：
构造过程，例如输入一行数据为:
6 2 1 2 3 2 5 1 4 5 7 2 2
则第一个参数6表示输入总共6个节点，第二个参数2表示头节点值为2
后续2个一组表示第2个节点值后面插入第1个节点值:
1 2 表示为 2->1，链表为2->1
3 2表示为 2->3，链表为2->3->1
5 1表示为 1->5，链表为2->3->1->5
4 5表示为 5->4，链表为2->3->1->5->4
7 2表示为 2->7，链表为2->7->3->1->5->4
最后生成的链表的顺序为 2 7 3 1 5 4
最后一个参数为2，表示要删掉节点值为 2 的节点
最终结果为 7 3 1 5 4
"""
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkList:
    def __init__(self, head=None):
        self.head = head
        self.nodes = []

    def insert(self, value, prevalue):
        p = self.head
        node = Node(value)
        while p is not None:
            if p.value == prevalue:
                node.next = p.next
                p.next = node
                break
            p = p.next

    def delete(self, value):
        temp = Node(0)
        temp.next = self.head
        p = temp
        while p.next is not None:
            if p.next.value == value:
                p.next = p.next.next
                break
            p = p.next
        self.head = temp.next

    def print(self):
        p = self.head
        while p is not None:
            self.nodes.append(p.value)
            p = p.next


if __name__ == "__main__":
    strs = input().split()
    nums = int(strs[0])
    head_value = int(strs[1])
    delete_value = int(strs[-1])
    head = Node(head_value)
    l = LinkList(head)
    for i in range(1, nums):
        l.insert(int(strs[2 * i]), int(strs[2 * i + 1]))
    l.delete(delete_value)
    l.print()
    nodes = l.nodes
    for n in nodes:
        print(n, end=" ")
