class LCSMatrix:
    
    def __init__(self, str1, str2):
        self.row_count = len(str1)
        self.column_count = len(str2)
        self.str1 = str1
        self.str2 = str2
        self.substrings = set()
        
        # oneliner matrix attribute, needs to be the length of each string only
        self.matrix = [[0 for _ in range(self.column_count)] for _ in range(self.row_count)]
        
        # oneliner for the DP table, each cell is the dict {}
        self.dp_matrix = [[{"length":0, "set":set()} for column in range(self.column_count)] for row in range(self.row_count)]
        
        # yet another grid for building a path through the matrix
        # ⬉ ⭠ ⭡
        self.path_matrix = [[0 for _ in range(self.column_count)] for _ in range(self.row_count)]
        
        
        #   s t r i n g 2
        # s 
        # t
        # r
        # i
        # n
        # g
        # 1
                        
        # build both the sequence match count matrix,                           
        # and a special matrix with dictionary that stores the same match count,
        # but also a set of the subsequence strings        
        for i in range(self.row_count):
            for j in range(self.column_count):
                
                # match, add 1 to the 
                if self.str1[i] == self.str2[j]:
                    
                    # a match is found in the position of up and left in the martix so 
                    # this means that there was a sequential match
                    match_count = self.get_entry(i - 1, j - 1) + 1
                    self.matrix[i][j] = match_count
                    
                    # dict{match_count: set("seq1", ...)}
                    # if there was a match, add the same match count to length
                    # then create set or add character to the set 
                    self.dp_matrix[i][j]["length"] = match_count
                    
                    # if either index is 0 then second column or the second row, create a new set and add the character
                    if i == 0 or j == 0:
                        self.dp_matrix[i][j]["set"].add(self.str1[i])
                    
                    # add 
                    else:
                        if self.dp_matrix[i - 1][j - 1]["set"]:
                            self.dp_matrix[i][j]["set"] = {subseq + self.str1[i] for subseq in self.dp_matrix[i - 1][j - 1]["set"]}
                        else:
                            self.dp_matrix[i][j]["set"] = {self.str1[i]}
                 
                # no match   
                else:
                    
                    # if no match then carry over previous matches from left or up
                    # take the largest match to indicate that is the current longest length
                    match_count = max(self.get_entry(i - 1, j), self.get_entry(i, j - 1))
                    self.matrix[i][j] = match_count
                    
                    # set the length
                    self.dp_matrix[i][j]["length"] = match_count
                    
                    # shift the set from longest match into into current cell 
                    if self.get_entry(i - 1, j) > self.get_entry(i, j - 1): # top
                        self.dp_matrix[i][j]["set"] = self.dp_matrix[i - 1][j]["set"]
                    
                    elif self.get_entry(i - 1, j) < self.get_entry(i, j - 1): # left
                        self.dp_matrix[i][j]["set"] = self.dp_matrix[i][j - 1]["set"]
                    
                    # if the same count is found in both adjacent cells,    0    {B}
                    # then the set will be the mutually exclusive strings   {A}  {A,B}
                    else:
                        self.dp_matrix[i][j]["set"] = self.dp_matrix[i - 1][j]["set"].union(self.dp_matrix[i][j - 1]["set"])
               
        
            
    def get_entry(self, row_index, column_index):
        
        # index between 0 and len(str)
        if 0 <= row_index < self.row_count and 0 <= column_index < self.column_count:
            return self.matrix[row_index][column_index]
        return 0
    
    # wind through the matrix recursively exploring all paths that have a matching character 
    def backtrack(self, i, j, subsequence):
            # recursive calls to backtrack will continue to decrement i and j
            # base case will trip as an index becomes negative
            # however function will still continue to run 
            # (some of these returns will just be a end of the path)
            # recursion loop 
            if i < 0 or j < 0:
                self.substrings.add(subsequence)
                return

            # check current cell and and recursively move up and left
            # add the current character to the subsequence
            if self.str1[i] == self.str2[j]:
                self.path_matrix[i][j] = "M"
                self.backtrack(i - 1, j - 1, self.str1[i] + subsequence)
                
            # other directions which left and up which according to the grid will have the SAME VALUE
            # once it is in that cell it will check again    
            else:
                
                # use the get_entry() method with bounds checking
                # up one row
                if self.get_entry(i - 1, j) == self.get_entry(i, j):
                    self.backtrack(i - 1, j, subsequence)
                # left one column
                if self.get_entry(i, j - 1) == self.get_entry(i, j):
                    self.backtrack(i, j - 1, subsequence)
                    
    # trigger recursive backtrack and returns 
    def get_longest_common_subsequences(self, recursive = True):
        if recursive:
            # if there is a 0 in the bottom right cell of grid, no subsequence was found
            if self.get_entry(self.row_count - 1, self.column_count - 1) == 0:
                return set()

            # this will initiate the recursion, building the set of substrings
            self.backtrack(self.row_count - 1, self.column_count - 1, "")
            return self.substrings
        else:
            return self.dp_matrix[self.row_count - 1][self.column_count - 1]["set"]
    
    
    ########################################################
    def get_column_count(self):
        return self.column_count
    def get_row_count(self):
        return self.row_count
    
    
    
test1 = LCSMatrix("ABBA", "BAAB")

# hacky formatting     
print("   ", end="")
for char in test1.str2:
    print(char, end="  ")
print()
for row in range(test1.row_count):
    print(f'{test1.str1[row]} {test1.matrix[row]}')
    
print(f'Set of Subsequences: {test1.get_longest_common_subsequences()}')
    
# for row in test1.path_matrix:
#     print(" ".join(str(element) for element in row))

