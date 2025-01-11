def sum_digits(n):
  if n < 10:
    return n
  else:
    last_digit = n % 10
    # What argument is every digit except the last?
    return last_digit + sum_digits(n//10)

  
print(sum_digits(12))
  # 3
print(sum_digits(194))

  # 14
print('bitchass')
  
  
  