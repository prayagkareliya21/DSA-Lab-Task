class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def insert_begin(self,data):
        new_node = Node(data)
        new_node.next=self.head
        self.head=new_node
    
    def insert_last(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
            
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next

l1 = SLL()
while True:
    print("1. insert begin")
    print("2. insert last")
    print("3. display")
    print("4. exit")
    ch=int(input("enter your choice="))

    if ch==1:
        data=int(input("enter node value="))
        l1.insert_begin(data)
    elif ch==2:
        data=int(input("enter node value="))
        l1.insert_last(data)
    elif ch==3:
        l1.display()
    elif ch==4:
        break
    else:
        print("invalid")
