# Define factorial() below:
def factorial(n):
  if n < 0: # if n is negative just return n 
    return n
  elif n == 1: # base case, if n == 1
    print("Current n value: {}".format(n))
    return n
  else:
    #print("Factorial step n greater than 1")
    print("Current n value: {}".format(n))
    return n * factorial(n-1)

print(factorial(500))

