from linked_list import Node, LinkedList
from blossom_lib import flower_definitions 

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for item in range(self.array_size)] # list of instances of LinkedList class
    
  def hash(self, key): # sums the unicode values ex: ord('A') == unicode value 65, chr(65) == char 'A'
    print("HASH\n########################")
    for char in key:
      print(f'Unicode value of {char} is {ord(char)}')
    print(f'Sum of unicode values: {sum(key.encode())}')
    # print("Hash Method: {}".format(sum(key.encode()))) 
    print("########################\n")

    return sum(key.encode())
  
  def compress(self, hash_code): # method makes sure that all hashcodes are within the bounds of the length of the array size
    print("Compress method: {}".format(hash_code % self.array_size))
    return hash_code % self.array_size

  def assign(self, key, value): # assigns an instance of Node(key, value) to the hashmap based of hashcode of key
    array_index = self.compress(self.hash(key))
    payload = Node([key, value])
    added_key = payload.get_value()[0]
    added_value = payload.get_value()[1]
    print("Adding KEY: {} with VALUE: {}".format(added_key, added_value))
    list_at_array = self.array[array_index]
    for item in list_at_array:
      if item[0] == key:
        item[1] = value
    list_at_array.insert(payload)

  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]
    print("Retrieve Method: {}".format(list_at_index))
    for item in list_at_index:
      if item is not None:
        if item[0] == key:
          return item[1]
        else:
          return None
      else:
        return None
    
  def get_map(self):
    for hash_map_item in self.array:
      for iterable_list in hash_map_item:
        print(type(iterable_list))

blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
  print(f'\n###############################################\n')
  blossom.assign(flower[0], flower[1])


blossom.get_map()












