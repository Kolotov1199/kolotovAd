class Person:
    def __init__(self, name, age, gender, characteristics):
        self.name = name
        self.age = age
        self.gender = gender
        self.characteristics = characteristics

def add_character(story):
    name = input("Введите имя нового персонажа: ")
    age = input("Введите возраст нового персонажа: ")
    gender = input("Введите пол нового персонажа: ")
    characteristics = input("Введите характеристики нового персонажа: ")
    new_person = Person(name, age, gender, characteristics)
    story.append(new_person)
    print("Новый персонаж успешно добавлен в историю!")