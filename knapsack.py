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
        knapsack_recursion(weight_cap, values, weights, n - 1)
        
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
        include_item = nth_value + knapsack_recursion(weight_cap - weights[n - 1], values, weights, n - 1)
        exclude_item = knapsack_recursion(weight_cap, values, weights, n - 1)
        return max(include_item,exclude_item)


def dynamic_knapsack(weight_cap, weights, values):
  rows = len(weights) + 1
  cols = weight_cap + 1
  # Set up 2D array
  matrix = [ [] for x in range(rows) ]

  # Iterate through every row
  for index in range(rows):
    # Initialize columns for this row
    matrix[index] = [ -1 for y in range(cols) ]

    # Iterate through every column
    for weight in range(cols):
      # Write your code here
      if index == 0 or weight == 0:
        # base case
        matrix[index][weight] = 0
        
      elif weights[index - 1] <= weight:
          # set the cell value = to the max between including or excluding item
          # 
          matrix[index][weight] = max(
              values[index - 1] + matrix[index - 1][weight - weights[index - 1]], 
              matrix[index - 1][weight],
              )
      else:
        # if we exceed the weight limit on the item then it means we have to exclude it by default
        # excluded items will be located one cell directly above over-weight cell 
        matrix[index][weight] = matrix[index - 1][weight]
        

  
  # Return the value of the bottom right of matrix
  for row in matrix:
    print(row)
    #print("\n")
  return matrix[rows-1][weight_cap]

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
print(dynamic_knapsack(weight_cap, weights, values))    
    
    