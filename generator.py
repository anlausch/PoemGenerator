import os
import codecs

with codecs.open("dbcntr.txt", "r") as f: 
  cnt = f.read().strip()
  
files = os.listdir("db")
poem = '\n'.join(codecs.open("db/" + cnt + ".txt", "r").read().split("#"))
with codecs.open("en-poem.txt", "w", encoding="utf8") as f:
  f.write(poem.strip())

with codecs.open("dbcntr.txt", "w", encoding="utf8") as f:
  f.write(str(int(cnt) + 1))
  


