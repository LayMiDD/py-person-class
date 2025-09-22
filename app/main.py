class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []

    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        result.append(Person(name, age))

    for person_dict in people:
        name = person_dict["name"]
        person_obj = Person.people[name]

        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            person_obj.wife = Person.people[wife_name]

        if "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            person_obj.husband = Person.people[husband_name]

    return result
