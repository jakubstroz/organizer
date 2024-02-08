class Note:
    next_index = 1
    def __init__(self) -> None:
        self.index = self.next_index
        self.__class__.next_index = self.next_index + 1
        print(f'tworzę notatkę nr {self.index}.')

    def add_text(self):
        self.text = input('Podaj treść notatki: \n')

    def edit_text(self):
        pass
    



notka1 = Note()
notka2 = Note()