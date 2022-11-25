## Q1
# 1) The benefits of using CSV files in Python is that it helps with ordering format.

# 2)
numList = input("Enter 5 numbers: ")

# 3)
file = open("numList.csv", "w")
dataIn = file.write(numList)
file.close()
print(dataIn)

# 4)
file = open("numList.csv", "r")
dataIn = file.read()
file.close()
print(dataIn)

# 5)
numList = dataIn.split(",")
numList = [int(i) for i in numList]

# 6)
print(numList)

# 7)
numList = list.sort()

# 8)
print(list)

# 9)


# 10)


# # 11)
# names = []

# # 12)
# pets = []

# # 13)
# nameInput = input("What is your name? ")
# petInput = input("How many pets do you have? ")

# # 14)
# names.extend(nameInput)
# pets.extend(petInput)

# 15)

## Q2
# (a) Abstraction is taking out the useless information in a question and only dealing with the important information.
# (b) Functions can be used by programmers to achieve abstraction by making a function that gets rid of unimportant information.

## Q3
# (a) 11111011
# (b) 2^7    2^6    2^5    2^4    2^3     2^2     2^1      2^0
#      1      1      1      1      1       0       1        1 
#     128    64     32     16      8       0       2        1
#     128 + 64 + 32 + 16 + 8 + 2 + 1 = 251

## Q4
##Anagrams are words that contain the same letters. Eg. car and arc are anagrams of each other 

def is_anagram(w1, w2): 
  if sorted(w1) == sorted(w2): 
    return True 
  else: 
    return False 

word1 = str(input("Enter the first word: "))
word2 = str(input("Enter the second word: "))

##Test whether the sorted strings are the same as each other 

##If the sorted strings are the same as each other then they must be anagrams 
if(sorted(word1) == (sorted(word2))): 
  print(word1, "is an anagram of", word2) 
elif(sorted(word1) != (sorted(word2))):
  print(word1, "is NOT an anagram of", word2)

phrase = input("Enter a phrase: ")
phrase = phrase.replace(" ","")
if(sorted(word1) == (sorted(phrase))):
  print(word1, "is an anagram of", phrase)
elif(sorted(word1) != (sorted(phrase))):
  print(word1, "is NOT an anagram of", phrase)

if(sorted(word2) == (sorted(phrase))):
  print(word2, "is an anagram of", phrase)
elif(sorted(word2) != (sorted(phrase))):
  print(word2, "is NOT an anagram of", phrase)
