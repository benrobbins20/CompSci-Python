def ks_dynamic(weight_cap, weights, values):
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
    
    
print(ks_dynamic(5, [1, 3, 5], [250, 300, 500]))

