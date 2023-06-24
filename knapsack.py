###################
# knapsack problem
# made a nice diagram of a length of 4 list
# shows the flow like the fib sequence and path through maximum knapsack value

def knapsack_recursion(weight_cap,values,weights,n):
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

weight_cap = 50    
values = [90, 60, 100, 120]
weights = [10, 10, 20, 30]
n = len(values)

max_ = knapsack_recursion(weight_cap,values,weights,n)
print(max_)    
    
    
    