class DLNode:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

class DList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):
        new_node=DLNode(val)
        new_node.next=self.head
        if self.head!=None:
            self.head.previous=new_node
        self.head=new_node
        return self
    def print_values(self):
        runner=self.head
        while runner!=None:
            print(runner.value)
            # if runner.previous!=None:
            #     print(f"prev node val: {runner.previous.value}")
            # else:
            #     print(f"prev node val: {runner.previous}")
            # if runner.next!=None:
            #     print(f"next node val: {runner.next.value}")
            # else:
            #     print(f"next node val: {runner.next}")
            runner=runner.next
        return self
    def add_to_back(self, val):
        new_node=DLNode(val)
        runner=self.head
        while runner.next!=None:
            runner=runner.next
        runner.next=new_node
        new_node.previous=runner
        return self
    def remove_from_front(self):
        self.head=self.head.next
        self.head.previous=None
        return self
    def remove_from_back(self):
        last_node=self.head
        while last_node.next.next!=None:
            last_node=last_node.next
        last_node.next=None
        return self
    def remove_val(self, val):
        if self.head.value==val:
            self.remove_from_front()
        else:
            runner=self.head
            while runner.next.value!=val and runner.next.next!=None:
                runner=runner.next
            if runner.next.value==val:
                runner.next.next.previous=runner
                runner.next=runner.next.next
        return self
    def insert_at(self,val,n):
        if n==0:
            self.add_to_front(val)
        elif n>0:
            insert_node=self.head
            index=0
            while n!=index+1 and insert_node.next!=None:
                insert_node=insert_node.next
                index+=1
            if insert_node.next==None:
                self.add_to_back(val)
            else:
                prev_node=insert_node
                next_node=insert_node.next
                insert_node.next=DLNode(val)
                insert_node.next.next=next_node
                insert_node.next.previous=prev_node
                insert_node.next.next.previous=insert_node.next
        return self

my_list = DList()
my_list.add_to_front("Jim")
my_list.add_to_front("Dwight")
my_list.add_to_front("Andy")

my_list2 = DList()
my_list2.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").add_to_back('extra').add_to_back('stuff').remove_val('abcd').insert_at('abcd', 4).print_values()