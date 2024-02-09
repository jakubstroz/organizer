import sys
from items import Note, Card, show_cards, reload_cards , show_notes, reload

if __name__ == "__main__":
    x, n = 9, 11
    print('ORGANIZER')
    while True:
        print('1 - notatki')
        print('2 - wizytówki')
        print('0 - wyjście')
        x = int(input(': '))

        if x == 1:
            n = 55
            while n != 0:
                
                print('1 - wyświetl notatki')
                print('2 - dodaj notatkę')
                print('0 - powrót')
                print('9 - wyjscie z programu')
                n = int(input(': '))

                if n == 1:
                    for line in show_notes():
                        print(line + '\n')
                
                if n == 2:
                    name = (reload() + 1)
                    name = Note()
                    name.add_text()

                if n == 9:
                    sys.exit(0)
            
        elif x == 2:
            n = 55
            while n != 0:
                
                print('1 - wyświetl wizytówki')
                print('2 - dodaj wizytówkę')
                print('0 - powrót')
                print('9 - wyjscie z programu')
                n = int(input(': '))

                if n == 1:
                   for line in (show_cards()):
                       print(': '.join(line[1:]))
                
                if n == 2:
                    namec = (reload_cards() + 1)
                    namec = Card()
                    name = input('Podaj imie i nazwisko: \n')
                    number = input('Podaj numer telefonu: \n')
                    namec.add_contact(name, number)

                if n == 9:
                    sys.exit(0)

        elif x == 0:
            sys.exit(0)