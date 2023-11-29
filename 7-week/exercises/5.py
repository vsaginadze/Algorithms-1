'''
Write a method that deletes the last node (if any) in a LinkedList.
'''

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head):
        self.head = head
    
    def print(self):
        n = self.head
        while n != None:
            print(n.val, end = " ")
            n = n.next
        print()
    
    def delete_last(self):
        assert self.head != None, "linked list is empty"
        n = self.head
        if n.next == None:
            self.head = None
            return
        
        while n.next.next != None:
            n = n.next
        n.next = None