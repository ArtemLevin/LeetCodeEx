import datetime
import json

# notes ={}


def showMenu():
    print('''Press 
        1 - to create a note
        2 - to save the note
        3 - to delete the note
        4 - to edit the note
        5 - to show the list of the notes
        6 - to show the note
        any other button - to exit''')

def choiceInput(notes):
    yourChoice = input('Your choice is ')
    if yourChoice == "1":
        print("to create a note")
        createNote(notes)
    elif yourChoice == "2":
        print("to save a note")
        saveNote(notes)
    elif yourChoice == "3":
        print("to delete a note")
        deleteNote()
    elif yourChoice == "4":
        print("to edit a note")
        editNote()
    elif yourChoice == "5":
        print("to show the list of the notes")
        showNotesFromMenu()
    elif yourChoice == "6":
        print("to show the note")
        showOneNote()
    else:
        print("to exit")
        return False

def readNoteFile():
    with open('noteFile.json', 'r') as file:
        content = file.read()
        notes = json.loads(content)
    return notes


def createNote(notes):
    noteHeader = input('Enter the header of your note: ')
    noteText = input('Enter the text of your note: ')
    noteCreationDate = datetime.datetime.now().strftime("%Y.%m.%d %H:%M");
    notes[len(notes)+1] = [noteCreationDate, noteHeader, noteText]
    saveRequest = input("Do you want to save the note? (y/n): ")
    if saveRequest == "y": saveNote(notes)
    elif saveRequest == "n":
        showMenu()
        choiceInput()


def saveNote(notes):
    with open('noteFile.json', 'w') as file:
        content = json.dumps(notes)
        file.write(content)
        print("Your note file has been saved successfully")
    showMenu()
    choiceInput()

def showOneNote():
    notes = readNoteFile()
    noteNumber = input("Enter the number of the note you want to show ")
    if int(noteNumber) in range(1, len(notes) + 1):
        print(f"Note number: {noteNumber}. \n   Note date: {notes[noteNumber][0]} \n   Note header: {notes[noteNumber][1].upper()} \n   Note text: {notes[noteNumber][2]}")
    else:
        print("There is no note with such number in notes")
    showMenu()
    choiceInput()

def showNotesFromMenu():
    notes = readNoteFile()
    filterRequest = input("Woukd you like to filter notes by date?  (y/n) ")
    if filterRequest == "y": dateFilter()
    elif filterRequest == "n":
        if len(notes) != 0:
            for k,v in notes.items():
                print(f"Note number: {k}. \n   Note date: {v[0]} \n   Note header: {v[1].upper()} \n   Note text: {v[2]}")
        else:
            print("There is no any note")
        showMenu()
        choiceInput()

def showNotes():
    notes = readNoteFile()
    for k,v in notes.items():
        print(f"Note number: {k}. \n   Note date: {v[0]} \n   Note header: {v[1].upper()} \n   Note text: {v[2]}")
    return notes

def deleteNote():
    print("What note do you want to delete?")
    notes = showNotes()
    noteNumber = input("Enter note number ")
    notes.pop(noteNumber)
    saveNote(notes)
    print("The note deleted successfully")
    showMenu()
    choiceInput()

def editNote():
    print("What note do you want to edit?")
    showNotes()
    noteNumber = input("Enter note number ")
    notes[int(noteNumber)][0] = datetime.datetime.now().strftime("%Y.%m.%d %H:%M");
    notes[int(noteNumber)][1] = input("Enter new header of the note: ")
    notes[int(noteNumber)][2] = input("Enter new text of the note: ")
    saveRequest = input("Do you want to save the note? (y/n): ")
    if saveRequest == "y": saveNote(notes)
    elif saveRequest == "n":
        showMenu()
        choiceInput()


def dateFilter():
    date_1 = input("Enter the left border of the date interval in format YYYY.MM.DD HH:MM ---> ")
    day_x = datetime.datetime.strptime(date_1, '%Y.%m.%d %H:%M')
    date_2 = input("Enter the right border of the date interval in format YYYY.MM.DD HH:MM ---> ")
    day_y = datetime.datetime.strptime(date_1, '%Y.%m.%d %H:%M')
    notes = readNoteFile()
    counter = 0
    for k, v in notes.items():
        day_i = datetime.datetime.strptime(v[0], '%Y.%m.%d %H:%M')
        if day_i > day_x and day_i < day_y:
            print(f"Note number: {k}. \n   Note date: {v[0]} \n   Note header: {v[1].upper()} \n   Note text: {v[2]}")
            counter += 1
    if counter == 0: print("There is any note in chosen interval")
    showMenu()
    choiceInput()

def main(choice):

    while choice:
        showMenu()
        choice = choiceInput()

main(True)