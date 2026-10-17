class LinkedList:
    
    def __init__(self):
        #makes a dummy node whihc makes stuff easier
        self.head = ListNode(-1);
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next #goes past the dummy head 
        i = 0; #itterater 
        while curr: #while it is not equal to i == index
            if i == index:
                return curr.val #returns the current
            i+= 1 #increments
            curr = curr.next #traverses
        return -1 #if it doenst get anything

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next: #if it was empty before
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr: #while i < index and curr is not null
            #move curr to node before target
            i += 1
            curr = curr.next
        if curr and curr.next: # if you reach teh spot
            if curr.next == self.tail:  #if you read the end of the linked list 
                self.tail = curr # you make the tail equal to the one before the tail
            curr.next = curr.next.next #skips the i index of linked list
            return True
        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = [] # makes an array
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
class ListNode:
    def __init__(self,val,next_node = None):
        self.val = val
        self.next = next_node

