from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val: int = val
        self.next: Optional['ListNode'] = next

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        if not self.head:
            return -1
        self.traverse = self.head
        count = 0
        while count != index:
            if self.traverse.next == None:
                return -1
            else:
                count += 1
                self.traverse = self.traverse.next

        return self.traverse.val

    def insertHead(self, val: int) -> None:
        temp = ListNode(val)
        temp.next = self.head
        self.head = temp

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = ListNode(val)

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        
        i = 0
        current = self.head
        while current.next:
            if i + 1 == index:
                current.next = current.next.next
                return True
            current = current.next
            i += 1
        return False
        
    def getValues(self) -> List[int]:
        lst = []
        current = self.head
        while current:
            lst.append(current.val)
            current = current.next
        return lst