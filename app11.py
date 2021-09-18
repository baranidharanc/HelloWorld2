class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


vikhram = Person("Vikhram Baranidharan")
vikhram.talk()

vaibav = Person("Vaibav Baranidharan")
vaibav.talk()