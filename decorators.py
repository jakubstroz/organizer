def save_note(func):
    def inside(*args):
        with open('notes.txt', 'a+') as file:
            file.write(func(*args) + '\n')
    return inside

def readnotes(func):
    def inside():
        with open('notes.txt', 'r') as file:
            return [(line.strip()) for line in file.readlines()]