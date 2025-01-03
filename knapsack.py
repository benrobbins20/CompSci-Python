###################
# knapsack problem
# made a nice diagram of a length of 4 list
# shows the flow like the fib sequence and path through maximum knapsack value
##################
# also made diagram of iterative approach using tabulation/memoization concepts
# iterative, does need recursive call in 
# TODO
# todo would be make an updating chart that fills in slowly so you can visualize the cells being populated 

def recursive_knapsack(weight_cap,values,weights,n):
    # max carrying cap
    # list of values
    # list of weights
    # n is index
    # for recursion, index will start from that last item
    # base case will be if the carrying capacity is met (weight_cap == 0) or index == 0
    
    if weight_cap == 0 or n == 0:
        # this will have already added the value of 0th index 
        # can just return 0 and exit recursion loop
        return 0
    
    elif weights[n-1] > weight_cap:
        # weight exceeds weight cap 
        # skip by recursive call to next index
        recursive_knapsack(weight_cap, values, weights, n - 1)
        
    else:
        # enter the recursive loop
        # function call return max value between if that item is included or not
        # if item is included, add value of item to return value, subtract weight of that item from the weight_cap, move to next item n - 1
        # else move on to the next item n - 1
        # with recursion the index will hit every index value, either add item or skip item
        # for simplicity, can think of the recursion loop as starting with 2 roots
        # one path including including first index compared 
        # and a path not including first index compared
        # from there each tree from I and E are compared for max 
        
        nth_value = values[n - 1]
        include_item = nth_value + recursive_knapsack(weight_cap - weights[n - 1], values, weights, n - 1)
        exclude_item = recursive_knapsack(weight_cap, values, weights, n - 1)
        return max(include_item,exclude_item)


def dynamic_knapsack(weight_cap, weights, values):
  rows = len(weights) + 1 # a row for every item, plus a row for no items
  cols = weight_cap + 1 # a column for every weight capacity left, a column for 0 weight capacity
  placeholder = -1
  
  # empty list for every row
  matrix = [[] for x in range(rows)]
  
  # for every empty list in matrix, create (weight cap + 1) placeholder entries
  for item in range(rows):
    matrix[item] = [placeholder for weight in range(cols)]
    
    # for every column (weight cap + 1) in the row, add the 0's for base case
    for weight in range(cols):
      
      # base case, no items, no weight
      if item == 0 or weight == 0:
        matrix[item][weight] = 0

      # compare item weight to current weight index, take the max of including or excluding item
      elif weights[item - 1] <= weight:
        
        # current item:
        # values[item - 1]
        
        # included item: 
        # values[item - 1] + matrix[item - 1][weight - weights[item - 1]]
        # up one row, shift left by difference of column index minus weight of current item
        # add diff cell's value to the current item value
        included_item = values[item - 1] + matrix[item - 1][weight - weights[item - 1]]
        
        # excluded item:
        # matrix[item - 1][weight]
        # up one row, same column index
        # max value is unchanged
        excluded_item = matrix[item - 1][weight]
        
        
        matrix[item][weight] = max(
          values[item - 1] + matrix[item - 1][weight - weights[item - 1]], # include item, adjust weight capacity
          matrix[item - 1][weight] # exclude item, take value from above cell (max value unchanged)
        )
        
        # else, the current item weight > index (weight larger than capacity), exclude item
      else:
        matrix[item][weight] = matrix[item - 1][weight] # value from above cell
        
  # max value has percolated its way down to the bottom right cell
  return matrix[-1][-1]
    
    
#####RECURSIVE KNAPSACK#########

weight_cap = 50    
values = [90, 60, 100, 120]
weights = [10, 10, 20, 30]
n = len(values)
#max_ = knapsack_recursion(weight_cap,values,weights,n)
#print(max_)    


#####DYNAMIC KNAPSACK#########
weight_cap = 50
weights = [31, 10, 20, 19, 4, 3, 6]
values = [70, 20, 39, 37, 7, 5, 10]
#print(dynamic_knapsack(weight_cap, weights, values))


print(dynamic_knapsack(5, [1, 3, 5], [250, 300, 500]))
    
    
