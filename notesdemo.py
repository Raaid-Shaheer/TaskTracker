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
    NewAddition={
      "note": "".join(sys.argv[2:]),
      "status": "in-progress" #default status
    }
   
    notesdemo.append(NewAddition)
    with open(FILENAME,"w") as f:
      json.dump(notesdemo,f,indent=4)
      print("Note Added Successfully:", NewAddition["note"])

  # list 
elif command == "list":
    # default show all items in the list
    if len(sys.argv)==2:
      notes_displayed= notesdemo
    else:
      subcommand = sys.argv[2].lower()
      if subcommand=="to-do":
        notes_displayed = [note for note in notesdemo if note['status']=="to-do"]
      elif subcommand=="in-progress":
        notes_displayed = [note for note in notesdemo if note['status']=="in-progress"]
      elif subcommand=="completed":
        notes_displayed = [note for note in notesdemo if note['status']=="completed"]
      else:
        print("Invalid subcommand: Use either to-do, in-progress, completed")
        sys.exit(1)
    if not notesdemo:
      print("No notes available to list.")
    else:
      for i, listThis in enumerate(notes_displayed,1):
        print(f"{i}.{listThis['note']} {listThis['status']}")

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
      old_note = notesdemo[note_index]["note"]

      notesdemo[note_index] = {
        "note": new_note,
        "status": notesdemo[note_index]["status"]
      }
      with open(FILENAME, "w") as f:
        json.dump(notesdemo, f, indent=4)
        print(f"Updated Note {note_index + 1}: {notesdemo[note_index]}") # note_index+1 makes it human readable instead of 0 index
        print(f"Old Note: {old_note}")
    except (ValueError, IndexError):
      print("Invalid Note Number")
# change status
elif command == "status":
  if len(sys.argv) < 4:
    print("format: python notesdemo.py status note_number new_status")
  else:
    try:
      note_index= int(sys.argv[2]) - 1
      new_status = sys.argv[3].lower()
      if new_status not in ["to-do","in-progress","completed"]:
        print("invalid status: Select either to do, in progress, completed")
      else:
        notesdemo[note_index]["status"] = new_status
        with open(FILENAME,"w") as f:
          json.dump(notesdemo,f,indent=4)
          print(f"Updated Status of {note_index + 1} is  {new_status}")
    
    except (ValueError,IndexError):
      print("Invalid Note Number")
else:
  print("Invalid Command: Use either add,list, delete,update please!")
