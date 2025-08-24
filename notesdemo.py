import json
import sys

FILENAME = "notesdemo.json"

#load notes
try:
  with open(FILENAME,"r") as f:
    notesdemo = json.load(f)
except FileNotFoundError:
  notesdemo=[]

#commands

if sys.argv[1]== "add":
  NewAddition = "".join(sys.argv[2:])
  notesdemo.append(NewAddition)
  with open(FILENAME,"w") as f:
    json.dump(notesdemo,f,indent=4)
    print("Note Added Successfully:", NewAddition)

elif sys.argv[1] == "list":
  for i, listThis in enumerate(notesdemo,1):
    print(f"{i}.{listThis}")
  