from decorators import save_note


class Note:
    next_index = 1
    def __init__(self) -> None:
        self.index = self.next_index
        self.__class__.next_index = self.next_index + 1

    @save_note
    def add_text(self):
        self.text = input('Podaj treść notatki: \n')
        return self.text
    
    @save_note
    def edit_text(self):
        self.text = input('Podaj nową treść notatki: \n')
        return self.text

def show_notes():
    with open('notes.txt', 'r') as file:
        return [(line.strip()) for line in file.readlines()]
    
#read a file to get a index of note

with open('notes.txt', 'r') as file:
    for i, line in enumerate(file.readlines()):
        if len(line.strip()) > 0:
            x = i
            name = ('note' + str(i))
            name = Note()
        #return x + 1


#reload()

if __name__ == "__main__":
    #notka1 = Note()
    #notka1.add_text()
    #notka2 = Note()
    #print(show_notes())
    note1.edit_text()