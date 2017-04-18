# first non repeating char
def first_non_repeating_letter(string):
    if not string: return ""
    string_lowercase = string.lower()
    count = {}
    for s in string_lowercase:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
    non_repeating_char = ""
    for char, num in count.items():
        if num == 1:
            non_repeating_char = char
            break
            #need to break!
          #loop through "string_lowercase" and get index
          #need to handle case when there is no repeating char
    if not non_repeating_char:
        return ""
    index = 0
    x = 0
    for x in range(0, len(string_lowercase)):
        if string_lowercase[x] == non_repeating_char:
            index = x
            #need to break again
            break
    non_repeating_char_correct_case = string[x]
          # return string[index] to get the right case
 
    print(non_repeating_char_correct_case)


first_non_repeating_letter("")

def first_non_repeating_letter_v2(string):
    if not string: return ""
    string_lowercase = string.lower()

    non_repeating_char = ""
    for char in string_lowercase:
      count = string_lowercase.count(char)
      print(count)
      if count == 1:
          non_repeating_char = char
          break
          #need to break!
          #loop through "string_lowercase" and get index
          #need to handle case when there is no repeating char
    if not non_repeating_char:
        return ""
    index = 0
    x = 0
    for x in range(0, len(string_lowercase)):
        if string_lowercase[x] == non_repeating_char:
            index = x
            #need to break again
            break
    non_repeating_char_correct_case = string[x]
          # return string[index] to get the right case
 
    print(non_repeating_char_correct_case)

first_non_repeating_letter_v2("Stress")
