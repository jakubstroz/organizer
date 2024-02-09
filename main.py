import sys
from note import Note , show_notes, reload

if __name__ == "__main__":
    x, n = 9, 11
    print('ORGANIZER')
    while True:
        print('1 - notatki')
        print('2 - wizytówki')
        print('0 - wyjście')
        x = int(input(':'))

        if x == 1:
            while n != 0:
                print('1 - wyświetl notatki')
                print('2 - dodaj notatkę')
                print('3 - edytuj notatkę')
                print('0 - powrót')
                print('9 - wyjscie z programu')
                n = int(input(':'))

                if n == 1:
                    for line in show_notes():
                        print(line + '\n')
                
                if n == 2:
                    name = (reload() + 1)
                    name = Note()
                    name.add_text()
                
                if n == 3:
                    name: Note() = reload()
                    name.edit_text()


                if n == 9:
                    sys.exit(0)