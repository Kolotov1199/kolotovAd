class Person:
    def __init__(self, name, age, gender, description, occupation):
        self.name = name
        self.age = age
        self.gender = gender
        self.description = description
        self.occupation = occupation

    def change_occupation(self, new_occupation):
        self.occupation = new_occupation
        print(f"Род занятий персонажа {self.name} изменен на {new_occupation}.")

def add_character(story, name, age, gender, description, occupation):
    new_character = Person(name, age, gender, description, occupation)
    story.append(new_character)
    print(f"Персонаж {name} успешно добавлен в историю.")
