import time


class Animal:
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        self.id = id(name)
        self.date = time.strftime("%d/%m/%Y")
        
    def set_adopted_date(self, date: str):
        self.date = date


def main():
    fido = Animal("fido", "cat")
    fido.set_adopted_date('24/12/2022')


main()
