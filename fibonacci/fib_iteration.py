def fibonacci(n): 
  if not isinstance(n,int):
    return 
  else:
    list_ = [0,1]
    #print(len(list_) - 1)
    if n <= len(list_) - 1: # meaning last digit of list_, or in the list already
      print('n is already in list, Return {}'.format(n))
      return list_[n]
    else:
      while n > len(list_) - 1:
        list_.append(list_[-1] + list_[-2])
        print(list_)
    print("Current n: {}".format(n))
    print("Current list length: {}".format(len(list_) - 1))    
    return list_[n]


# test cases
print(fibonacci(3) == 2)
print(fibonacci(7) == 13)
print(fibonacci(0) == 0)