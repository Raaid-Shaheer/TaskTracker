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
  print("Please follow the format:python filename command argument")
  sys.exit(1)

command = sys.argv[1]

#add note
if command == "add":
  if len(sys.argv) <3:
    print("Please add a note to add after the command")
  else:
    NewAddition = "".join(sys.argv[2:])
    notesdemo.append(NewAddition)
    with open(FILENAME,"w") as f:
      json.dump(notesdemo,f,indent=4)
      print("Note Added Successfully:", NewAddition)

  # list all 
elif command == "list":
    if not notesdemo:
      print("No notes available to list.")
    else:
      for i, listThis in enumerate(notesdemo,1):
        print(f"{i}.{listThis}")

# delete a note

elif command == "delete":
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

# Update note

elif command == "update":
  if len(sys.argv) < 4:
    print("format: python notesdemo.py update note_number updated_text")
  else:
    try:
      note_index = int(sys.argv[2]) - 1  # to make this 0-index
      new_note = " ".join(sys.argv[3:])  # to make the added note into a single string
      old_note = notesdemo[note_index]
    
      notesdemo[note_index] = new_note
      with open(FILENAME, "w") as f:
        json.dump(notesdemo, f, indent=4)
        print(f"Updated Note {note_index + 1}: {notesdemo[note_index]}") # note_index+1 makes it human readable instead of 0 index
        print(f"Old Note: {old_note}")
    except (ValueError, IndexError):
      print("Invalid Note Number")

else:
  print("Invalid Command: Use either add,list, delete,update please!")
