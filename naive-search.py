# Define pattern_search
def pattern_search(text, pattern):
  # santize input
  if not isinstance(text,str):
    text = str(text)
  if not isinstance(pattern,str):
    pattern = str(pattern)
  pattern = pattern.strip() # strip leading and trailing spaces or line breaks
  if " " not in pattern:
    text = text.replace(" ","") # remove all spaces from text #ONLY# if a space/" " isn't in the stripped pattern, which will be 99% of time
  if len(pattern) < len(text): # close script if text isn't big enough for the pattern to fit
    matches_accum = 0 # seperate global counter to prevent the script from running if maximum possible matches has been found
    redundant_copy_of_text = text # keep original
    max_poss = len(text) // len(pattern) # integer representing how many times the pattern can feasibliy go into the text itself
    max_index = len(text) - 1 # maximum index of the text, can't exceed bounds so if checking index, need to make sure text_index <= max_index
    print("#"*50)
    print(f"Maximum index of text={max_index}\nMaximum match possibilities={max_poss}\nOriginal text={text}\nPattern={pattern}")
    print("#"*50)
    print()
  else:
    print('Text is shorter than pattern, quitting')
    return
 
  # start this bitch 
  
  for text_index in range(len(text)): # OUTER LOOP
    match_count = 0 # set the resetting match count, resets after iterated completely through inner loop
    if len(text) < len(pattern):
      print(f"Quitting, length of text too short\nText={text}\nPattern={pattern}")
      break
    if matches_accum == max_poss:
      print("Maximum matches have been met") # will break if hit the max possible matches
      break
    if text[text_index] == pattern[0]: # triggers at every instance in text where digit matches first digit of patter
      print(f"matching first digit:{text[text_index]}:{pattern[0]}; text index={text_index}") # this print statement is useful to check when first char of pattern matches text
    for pattern_index in range(len(pattern)): # INNER LOOP
      advanced_index = pattern_index+text_index
      if advanced_index <= max_index: # fixes index error, can set max_ind but when trying to access index it would exceed bound of text, has to pass this block to find a match
        
        if pattern[pattern_index].upper() == text[advanced_index].upper(): # compare the chars
          match_count += 1
        else: # this blocks starts feature of code that detects the correct sequence > 1 char of pattern but FAILS to complete the pattern aka ##DUD##
          if match_count > 1:
            print()
            print("!"*10)
            print(f"DUD with {match_count} chars in row")
            print(f"Failed match={text[text_index:text_index+match_count]}")
            print("!"*10)
          break
        if match_count == len(pattern): #######SUCCESS BLOCK
          found_slice = text[text_index:len(pattern)+text_index]
          print(f"found {pattern} in text at slice [{text_index}:{text_index+len(pattern)}]\npattern={pattern}:text slice={found_slice}") # success message
          if found_slice == pattern: # redundant check, this code may be unstable as the matches only increments when strings are compared ##MAY BREAK##
            matches_accum += 1
          elif found_slice.upper() == pattern.upper(): # if pattern did not match first check case before failing match
            matches_accum += 1
          else:
            # something definitely wrong if made it this far
            return

      else: # if advance_index exceeded the text from the current text_index + pattern_index ( pattern index increasing when iterating)
        # No more space left to check, exit loop
        break
    # outside of INNER loop
    # this runs after immediately after inner loop 
    if match_count == len(pattern): # this is a redundant check if a match was successful current text index
      # execute only if fulfilled matches_accum
      if (matches_accum > 0):
        print("success")
    
  # outside of both loops
  print(f"matches: {matches_accum}")

 
text = "NENEEDLENEEDNEEDHAYHAYNEEDLENE"
pattern = "NEEDLE"
# Invoke pattern_search
# pattern_search(text, pattern) # working good!




text2 = "SOMEMORERANDOMWORDSTOPATTERNSEARCHTHROUGH"
pattern2 = "pattern"

# pattern_search(text2, pattern2)




text3 = "This   still      works with    spaceswor ks"
pattern3 = "works"
# pattern_search(text3,pattern3)


text4 = 72261545782461270042268217942992552072047396
pattern4 = 42

pattern_search(text4,pattern4)