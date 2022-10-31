"""


"""

class ListNode:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.root = ListNode()
        temp = ListNode(prev=self.root)
        self.root.next = temp
        self.length = 0

    def get(self, index:int) -> int:
        if index >= self.length:
            return -1
        cur = self.root.next
        for i in range(index):
            # if cur is None:
            #     return -1
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        temp = ListNode(val=val, next=self.root.next, prev=self.root)

        if self.root.next:
            self.root.next.prev = temp

        self.root.next = temp
        self.length += 1

    def addAtTail(self, val:int) -> None:
        cur = self.root
        while cur:
            if cur.next is None:
                cur.next = ListNode(val, None, cur)
                self.length += 1
                return
            cur = cur.next


    def addAtIndex(self, index: int, val: int) -> None:
        cur, past = self.root.next, self.root
        if index >= self.length:
            return
        for i in range(index):
            # if cur is None:
            #     return
            past, cur = cur, cur.next

        temp = ListNode(val, cur, past)
        past.next = temp
        if cur:
            cur.prev = temp
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        cur, past = self.root.next, self.root
        for i in range(index):
            past = cur
            cur = cur.next
        past.next = cur.next
        if cur.next:
            cur.next.prev = past




