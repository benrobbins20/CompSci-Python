
# very hard to understand but follow the temp_cmbo after every step 

def power_set(my_list):
    print("\n\nstart#################")
    if len(my_list) == 0:
        return [[]]
    # recursive step: subsets without first element
    print("List before recursion: {}".format(my_list))
    if len(my_list) == 1:
        print('list length: 1, Proceeding...') 
    power_set_without_first = power_set(my_list[1:])  # why does it move forward when len(my_list) == 1??? because the value of power_set(my_list[1:]) RETURNS [] Therefore the recursion loop stops, and then will continue to next line 
    print("$$$$$$$")
    print("my_list full: {}".format(my_list))
    print("Power set without first: {}".format(power_set_without_first)) # should be empty list (within main list)
    print("current my_list[0]: {}".format(my_list[0]))
    print("$$$$$$$")
    # subsets with first element
    # should still be a value at my_list[0]
    with_first = [[my_list[0]] + rest for rest in power_set_without_first]
    print()
    print("with_first list: {}".format(with_first))
    print()
    print("without_first list: {}".format(power_set_without_first))
    print()
    # return combination of the two
    temp_combo = (with_first + power_set_without_first)
    print("current with_first: {}".format(with_first))
    print("current without first: {}".format(power_set_without_first))
    print(temp_combo)
    print("end#################\n\n")
    
    return with_first + power_set_without_first
  
universities = ['A','B','C']

power_set_of_universities = power_set(universities)

for set in power_set_of_universities:
  print(set)
#print(power_set_of_universities)
