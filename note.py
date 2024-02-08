from decorators import save_note, readnotes


class Note:
    next_index = 1
    def __init__(self) -> None:
        self.index = self.next_index
        self.__class__.next_index = self.next_index + 1
        print(f'tworzę notatkę nr {self.index}.')

    @save_note
    def add_text(self):
        self.text = input('Podaj treść notatki: \n')
        return self.text
    
    @save_note
    def edit_text(self):
        self.text = input('Podaj nową treść notatki: \n')
        return self.text
    
    def show_notes(self):
        with open('notes.txt', 'r') as file:
            return [(line.strip()) for line in file.readlines()]
        return self.index + self.text
    
#read a file to get a index of note
with open('notes.txt', 'r') as file:
    for i, line in enumerate(file.readlines()):
        if len(line.strip()) > 0:
            i = Note()

notka1 = Note()
notka1.add_text()
notka2 = Note()
print(notka1.show_notes())