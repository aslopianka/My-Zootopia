import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def get_animals_data():
    animals_data = load_data('animals_data.json')

    for animal in animals_data:
        if name := animal.get('name'):
            print(f"Name: {name}")

        char = animal.get('characteristics', {})
        if a_type := char.get('type'):
            print(f"Type: {a_type}")

        if diet := char.get('diet'):
            print(f"Diet: {diet}")

        if location := animal.get('locations', [None]):
            print(f"Location: {location[0]}")

        print()



def main():
    get_animals_data()


if __name__ == "__main__":
    main()