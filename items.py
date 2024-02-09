from decorators import save_note, save_card
import csv


class Note():
    next_index = 1
    def __init__(self) -> None:
        self.index = self.next_index
        self.__class__.next_index = self.next_index + 1

    @save_note
    def add_text(self):
        self.text = input('Podaj treść notatki: \n')
        return self.text
    


def show_notes():
    with open('notes.txt', 'r') as file:
        return [(line.strip()) for line in file.readlines()]
    
#read a file to get a index of note
def reload():
    x = 1
    with open('notes.txt', 'r') as file:
        for i, line in enumerate(file.readlines()):
            if len(line.strip()) > 0:
                x = i
                i = Note()
        return x
    


class Card():
    next_index = 1
    def __init__(self) -> None:
        self.index = self.next_index
        self.__class__.next_index = self.next_index + 1

    @save_card
    def add_contact(self, name, number):
        return name, number



def show_cards():
    with open('cards.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        return [row for row in csvreader]

def reload_cards():
    x = 1
    with open('cards.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for i, line in enumerate(csvreader):
            if len(line) > 0:
                x = i
                i = Note()
        return x


reload()
reload_cards() 
