#!/opt/homebrew/bin/python3
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    
    def get_value(self):
        return self.value
  
    
    def get_next_node(self):
        return self.next_node
  
    
    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)
        print('New Linked List started')
  
    
    def get_head_node(self):
        return self.head_node
  
    
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    
    
    def add_node(self,value):
        print('Adding new node with value: {}'.format(value))
        new_node = Node(value)
        if self.head_node == None: #LL is empty we add new node to beginning
            print('Added head node: {}'.format(value))
            #iterate to last node and then add the new node
            self.head_node = new_node
        else:
            current_node = self.head_node
            while current_node:
                if current_node.get_next_node() == None:
                    #add new node here
                    current_node.set_next_node(new_node)
                    return
                else:
                    current_node = current_node.get_next_node()

    
    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list
  
 
    def remove_node(self,value_to_remove):
        current_node = self.get_head_node() #starting at beginning of LL
        if current_node.get_value() == value_to_remove: # if head node value needs removed, juxt set head node to next node
            print('Found value to remove')
            self.head_node = current_node.get_next_node()
        else: #value_to_remove not at beginning of list
            while current_node: # while the is a current node variable set (not None)
                current_next_node = current_node.get_next_node()
                if current_next_node.get_value() == value_to_remove:
                    current_node.set_next_node(current_next_node.get_next_node())
                    current_node = None #leaving loop 
                else:
                    current_node = current_next_node


    def swap_nodes(self, val1, val2):
        print(f'Swapping {val1} with {val2}')
        #setting all 4 pointers with default values so we can search for values
        node1_prev = None
        node2_prev = None
        node1 = self.head_node
        node2 = self.head_node

        if val1 == val2:
            print("Elements are the same - no swap needed")
            return

        while node1 is not None: # will interate through whole list until node1.get_next_node() == None, then will exit in next code block
            if node1.get_value() == val1:
                break
            node1_prev = node1
            node1 = node1.get_next_node()

        while node2 is not None:
            if node2.get_value() == val2:
                break
            node2_prev = node2
            node2 = node2.get_next_node()

        if (node1 is None or node2 is None): # will exit out of program if node1 or node2 == None
            print("Swap not possible - one or more element is not in the list")
            return

        if node1_prev is None:
            self.head_node = node2
        else:
            node1_prev.set_next_node(node2)

        if node2_prev is None:
            self.head_node = node1
        else:
            node2_prev.set_next_node(node1)

        temp = node1.get_next_node()
        node1.set_next_node(node2.get_next_node())
        node2.set_next_node(temp)




ll = LinkedList('Start')
print(ll.stringify_list())
ll.add_node('Next')
print(ll.stringify_list())
ll.add_node('value')
ll.add_node('boobies')
print(ll.stringify_list())
ll.insert_beginning('mega boobies')
print(ll.stringify_list())

ll = LinkedList()
for i in range(10):
    ll.insert_beginning(i)
print(ll.stringify_list())
ll.swap_nodes(0,9)
print(ll.stringify_list())






















            
          

      









