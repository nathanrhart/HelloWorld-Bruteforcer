from random import *
import time
#char 0 - 1114111
hi = input("")

place = 0
word = "hello world"
refreshrate = 5000
progress = ""
start = time.time()
count = 0
printed = False
while printed == False:
  letter = chr(randint(0,1114111))
  if count == refreshrate:
    try:
      print(str(progress) + str(letter))
      count = 0
    except:
      count = refreshrate - 1

  count += 1
      
  if letter == word[place]:
    progress += (word[place])
    place += 1

  if len(progress) == len(word):
    print(progress)
    end = time.time()
    print("Time in seconds: " + str(end - start))
    break
    
    
  
  
