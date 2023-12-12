def add_character(story, name, age, gender, description):
    new_character = Person(name, age, gender, description)
    story.append(new_character)
    print(f"Персонаж {name} успешно добавлен в историю.")