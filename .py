
#Import libraries
import os           #For reading file
import re           #sub - For removing numbers
import pandas as pd #For data frame operations
import string

#import numpy  as np
#Read the file
os.path.abspath(os.getcwd())
fileread = open("textdoc.txt", "r", encoding="utf8")
file = fileread.read()

#Data Cleaning Function

def data_cleaning(file):
  #1. Removing Punctuations
  file = file.translate(str.maketrans('', '', string.punctuation))
  
  #2. Removing Apostrophe
  file = file.replace("'", "")
  
  #3. Converting all words to Lowercase
  file = file.lower()

  #3. Removing Numbers
  file_cleaned      = re.sub(r'\d+', '', file)
  
  return file_cleaned

file_cleaned = data_cleaning(file)

#To pass the previous chunk output to this chunk everytime it is executed
file = file_cleaned

#For splitting the file in different lines
file = file.splitlines()
#For removing WhiteSpaces
file = filter(lambda x: not re.match(r'^\s*$', x), file)

file = pd.DataFrame(file)
#Splitting the file into 2 parts - file1 containing first 5000 lines and file2 containing the rest
file1 = file[:5000]
file2 = file[5000:]

file1_map = file1
file2_map = file2

words1 = []
for i in range(len(file1_map)):
  line = file1_map.iloc[i]
  string = line.to_string()
  string = string[1:]
  words = string.split()
  words1.extend(words)      #Used here to append multiple lists into one list

words2 = []
for i in range(len(file2_map)):
  line = file2_map.iloc[i]
  string = line.to_string()
  string = string[1:]
  words = string.split()
  words2.extend(words)      #Used here to append multiple lists into one list

words1_map = words1
words2_map = words2

words_mapper = pd.DataFrame(words1_map)
words_mapper[1] = '1'
words_mapper.columns = ['Key', 'Value']
print (words_mapper[1:9].to_string(index=False, header=None))
#Printing below are some of the Key value pairs obtained after the Mapper function -

words_reducer = words_mapper
words_reducer = words_reducer.groupby('Key')
#print(words_mapper)
print(words_reducer.agg(np.count_nonzero))

fileread.close()
