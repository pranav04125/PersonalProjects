from xml.etree.ElementTree import QName


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next =  next
        
    def __repr__(self):
        return repr(self.value)

class LinkedList:
    def __init__(self):
        self.head = Node()

    def __repr__(self) -> str:
        output = "LinkedList("

        current = self.head

        while current.next:        
            current = current.next
            output += repr(current) + ", "
        return output[:-2] + ')'

    def append(self, value):
        current = self.head

        while current.next:
            current = current.next
        
        current.next = Node(value)
    
    def pop(self):
        current = self.head

        while current.next.next:
            current = current.next
        
        current.next = None

def main():
    mylist = LinkedList()
    mylist.append(1)
    mylist.append(2)
    mylist.append(3)
    print(mylist) 

    mylist.pop()
    print(mylist)

if __name__ == "__main__":
    main()