class DLNode:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

class DList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_to_front(self, val):
        new_node=DLNode(val)
        if self.tail==None:
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.previous=new_node
        self.head=new_node
        return self
    def print_values(self):
        runner=self.head
        while runner!=None:
            print(runner.value)
            # print(f"head {self.head.value}")
            # print(f"tail {self.tail.value}")
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
        if self.head==None:
            self.head=new_node
        else:
            new_node.previous=self.tail
            self.tail.next=new_node
        self.tail=new_node
        return self
    def remove_from_front(self):
        if self.head!=None:
            self.head=self.head.next
            self.head.previous=None
        return self
    def remove_from_back(self):
        if self.tail!=None:
            self.tail=self.tail.previous
            self.tail.next=None
        return self
    def remove_val(self, val):
        if self.head!=None and self.head.value==val:
            self.remove_from_front()
        elif self.head!=None:
            runner=self.head
            while runner.next.value!=val and runner.next.next!=None:
                runner=runner.next
            if runner.next.value==val and runner.next.next!=None:
                runner.next.next.previous=runner
                runner.next=runner.next.next
            elif runner.next.value==val and runner.next.next==None:
                self.remove_from_back()
        return self
    def insert_at(self,val,n):
        if n==0:
            self.add_to_front(val)
        elif n>0 and self.head!=None and self.tail!=None:
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
        else:
            self.add_to_front(val)
        return self

my_list2 = DList()
my_list2.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").add_to_back('extra').add_to_back('stuff').remove_val('abcd').insert_at('abcd', 76).remove_from_back().print_values()