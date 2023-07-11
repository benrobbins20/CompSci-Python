def make_list(str1,str2):
  str1_lst = []
  str2_lst = []
  for char in str1:
    str1_lst.append(char)
  for char in str2:
      str2_lst.append(char)
  compare_grid = (str1_lst,str2_lst)
  for compare_list in compare_grid:
      print(compare_list)
    
def longest_common_substring(string1,string2):
  make_list(string1,string2)
  # column are each char from string 1
  # rows are each char from string two
  # ADD len() + 1 because there is a possiblilty of not
  ## including char
  # create both with one-liner comprehensions
  grid = [[0 for col in range(len(string1) + 1)] for row in range(len(string2) + 1)]
  
  # ROWS = string2
  # COLS = string1

  # cant really iterate throughs rows explicitly, so can just iterate through the same range as what that rows are which is range(1, len(string2) + 1)
  # wait isnt that just the same as range(len(string2) + 1) ????
  
  #print(range(len(string2) + 1)) # range(0,7) == 7
  #print(range(1,len(string2)+1)) # range(1,7) == 6
  for row_ind in range(1, len(string2) + 1):
    # this is len(6) 
    print("Comparing: {0}".format(string2[row_ind - 1]))
    # must decrement row because we need actual index location
    # compare inner loop 
    for col_ind in range(1,len(string1) + 1):
      #print("Against: {0}".format(string1[col_ind - 1]))
      # check the string char at same position
      if string1[col_ind - 1] == string2[row_ind - 1]:
        print("Match:row{0}:col{1}".format(row_ind,col_ind))
        # then we have a string/char match
        # (at least one match)
        # if there is a match, then set that cell equal to the previous cells value PLUS ONE. we are counting up
        # confused on this part, why do we add to the cell, i thought cell value was a .. value
        # but the cell value is an integer of match size??
        # the previous cell has match size of n
        # and if we have a match, the match size equals n+1
        grid[row_ind][col_ind] = grid[row_ind-1][col_ind-1] + 1
      else:
        print("no match at row{0}:col{1}".format(row_ind,col_ind))
        # chars don't match
        # put the max value of grid[last_row][current column]
        # and grid[current row][last column]
        grid[row_ind][col_ind] = max(grid[row_ind-1][col_ind],grid[row_ind][col_ind-1])

  # print the grid
  for row in grid:
    print(row)
    
  # geez how did I not know that i can access a loop variable outside of the loop, crazy, 
  # at this point out of the loop the row_ind and col_ind are at their max which is 6 
  # 0,7 == length of 7;0,1,2,3,4,5,6  
  substr = []
  # print(row_ind,col_ind) # 6 6
  # print(string2[row_ind-1], string1[col_ind-1]) # last char in the index
  while row_ind > 0 and col_ind > 0:
    # starting at the highest index
    if string1[col_ind-1] == string2[row_ind-1]:
      # the last characters match
      # add to substr
      # decrement column index and row index
      substr.append(string1[col_ind-1])
      row_ind -= 1
      col_ind -= 1
    elif grid[row_ind-1][col_ind] > grid[row_ind][col_ind-1]:
      row_ind -= 1
    else:
      col_ind -= 1
   
  print(substr)
    
   
  
dna_1 = "ACCGTT"
dna_2 = "CCAGCA"
longest_common_substring(dna_1,dna_2)