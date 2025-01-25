class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


def mergeNodes(head):
    point = head
    while point != None:
        if point.next.val != 0:
            point.val += point.next.val
            point.next = point.next.next
        elif point.next.next == None:
            point.next = point.next.next
            point = point.next
        else:
            point = point.next
    return head


if __name__ == '__main__':
    pt = [0, 3, 1, 0, 4, 5, 2, 0]
    head = Node(pt[0])
    p = head
    for i in range(1, len(pt)):
        p.next = Node(pt[i])
        p = p.next
    head = mergeNodes(head)
    q = head
    while q != None:
        print(q.val)
        q = q.next