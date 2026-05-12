import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def get_animals_data():
    animals_data = load_data('animals_data.json')

    output_string = ""
    for animal in animals_data:
        if name := animal.get('name'):
            output_string += '<li class="cards__item">'
            output_string += f"Name: {name}<br/>\n"

        char = animal.get('characteristics', {})
        if a_type := char.get('type'):
            output_string += f"Type: {a_type}<br/>\n"

        if diet := char.get('diet'):
            output_string += f"Diet: {diet}<br/>\n"

        if location := animal.get('locations', [None]):
            output_string += f"Location: {location[0]}<br/>\n"
            output_string += '</li>'

    return output_string


def read_html_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def write_html_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


def main():
    animal_data = get_animals_data()
    html_content = read_html_file('animals_template.html')
    html_content = html_content.replace('__REPLACE_ANIMALS_INFO__', animal_data)
    write_html_file('animals.html', html_content)



if __name__ == "__main__":
    main()