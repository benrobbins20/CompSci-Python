def find_min(list_=None, min_=None):
  if list_ == []: # base case
    return min_
  else:
    if not min_ or (list_[0] < min_):
      min_ = list_[0]
    print("current min: {}".format(min_))
    print("Passing list: {} and Min: {}".format(list_[1:], min_))
    print(list_[1:] == []) # this IS TRUE,
    # so on the recursive call that is the last one, ex [67] --> list_[1:] is empty list
    return find_min(list_[1:], min_)



# test cases
print(find_min([42, 17, 2, -1, 67]) == -1)
print()
print(find_min([]) == None)
print()
print(find_min([13, 72, 19, 5, 86]) == 5)