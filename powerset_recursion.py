def power_set(my_list):
    # base case: an empty list
    if len(my_list) == 0:
        return [[]]
    # recursive step: subsets without first element
    print("List before recursion: {}".format(my_list))
    if len(my_list) == 1:
        print('Length of 1!!!, power_set([1:]) == Empty list: {}'.format(power_set(my_list[1:])))
    power_set_without_first = power_set(my_list[1:])  # why does it move forward when len(my_list) == 1??? because the value of power_set(my_list[1:]) RETURNS [] Therefore the recursion loop stops, and then will continue to next line 
    print('###################')
    print(power_set_without_first) # should be empty list (within main list)
    # subsets with first element
    # should still be a value at my_list[0]
    with_first = [[my_list[0]] + rest for rest in power_set_without_first]
    print("with_first list: {}, Length of list: {}".format(with_first,len(with_first)))
    print()
    print("without_first list: {} length of list: {}".format(power_set_without_first,len(power_set_without_first)))
    print()
    # return combination of the two
    print('end of function, returning')
    print(with_first)
    print(power_set_without_first)
    return with_first + power_set_without_first
  
universities = ['A','B','C']

power_set_of_universities = power_set(universities)

#for set in power_set_of_universities:
  #print(set)
print(power_set_of_universities)
