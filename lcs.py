from time import sleep
def longest_common_substring(str1, str2):
    result = ""
    len1, len2 = len(str1), len(str2)
  
    # iterate over all substrings of str1
    # print(range(1,len1+1))
    # print(range(len1)) # list(1,10)
    for i in range(len1):
        # for i in 0-9 (HelloWorld)
        # repeats 10 times
        for len_sub in range(i+1, len1+1):
            # loop var is 0th, so i + 1
            # to include last char we need len() + 1
            
            # get the substring from str1
            sub = str1[i:len_sub]
            # str1[0,1] = H
            # str1[0,2] = He
            # Hel
            # Hell
            # Hello
            # str1[1,2] # "e"
            # e
            # el
            # ell
            # ello
            
            print(f"Substring: {sub}, string index: {len_sub}, {range(i,len_sub)}")
            sleep(.5)
            # check if this substring is present in str2 and is
            # greater than the result
            #if sub in str2 and len(sub) > len(result):
                #result = sub
  
    #return result
str1 = "HelloWorld"
str2 = "WorldHello"
print(longest_common_substring(str1,str2))