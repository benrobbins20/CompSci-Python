def pattern_search(text, pattern, replacement=None, case_sensitive=True):
  fixed_text = "" 
  index_skipper = 0 # global variable to keep track of number of skips to correct text index iteration,
  # allows that outer loop to just skip the 
  for index in range(len(text)):
    if index_skipper > 0:
      #print(f"index={index} index skipper={index_skipper}") # keeps track of text index
      index_skipper -= 1
      continue # NO OP
    match_count = 0
    for char in range(len(pattern)): 
      if case_sensitive and pattern[char] == text[index + char]:
        match_count += 1
      elif not case_sensitive and pattern[char].lower() == text[index + char].lower(): 
        match_count += 1
      else:
        break
    if match_count == len(pattern):
      print(pattern, "found at index", index) # will be index we left off on
      # found pattern now, is replacement==True?
      if replacement != None:
          fixed_text += replacement
          # now need to advance text_index?? Can you do that?
          print(f"len pattern = {len(pattern)}, text_index={index}")
          index_skipper += len(pattern) - 1
          print("starting index_skipping") 
    else:
        fixed_text += text[index]
        
  print(fixed_text)
  return(fixed_text)

    
        
      
language = "Language Language Language Language Language"
#pattern_search(language, "Language", "language")



friends_intro = "Pylhon is a wonderful Language that zzz is beloved for its ease zzz of use and simple syntacs. While zzz at some times the performance can be less than iDil, by properly zzz utilizing built-in libraries and other languuUuage features, pylhon's performance zzz can approach that of C."
#friends_intro = "Pylhon is a wonderful Language that zzz "
#friends_intro = pattern_search(friends_intro, "pylhon", "Python", False)
#friends_intro = pattern_search(friends_intro, "idil", "ideal", False)
#print(friends_intro)
#friends_intro = pattern_search(friends_intro, "zzz ", "")

#friends_intro = pattern_search(friends_intro, "syntacs", "syntax")
#friends_intro = pattern_search(friends_intro, "languuUuage", "language")


pattern_search(friends_intro, "zzz ", "")
