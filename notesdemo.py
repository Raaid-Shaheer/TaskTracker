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

# check if command is given

if len(sys.argv) <2:
  print("Please follow the format: filename function note")
  sys.exit(1)
#add task
if sys.argv[1]== "add":
  NewAddition = "".join(sys.argv[2:])
  notesdemo.append(NewAddition)
  with open(FILENAME,"w") as f:
    json.dump(notesdemo,f,indent=4)
    print("Note Added Successfully:", NewAddition)
# list all tasks
elif sys.argv[1] == "list":
  for i, listThis in enumerate(notesdemo,1):
    print(f"{i}.{listThis}")

# delete a task

elif sys.argv[1] == "delete":
  if len(sys.argv) <3:
    print("Pleasee enter the note number you want to delete after the command delete")
  else:
    try:
      note_index = int(sys.argv[2]) - 1 # to make this 0-index
      deleted_note= notesdemo.pop(note_index)
      with open(FILENAME,"w") as f:
        json.dump(notesdemo,f,indent=4)
        print(f"Deleted Note: {deleted_note}") 
    except(ValueError,IndexError):
      print("Invalid Note Number") 
