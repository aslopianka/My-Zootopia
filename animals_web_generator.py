import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def serialize_animal():
    animals_data = load_data('animals_data.json')

    output_string = ""
    for animal in animals_data:
        name = animal.get('name')
        char = animal.get('characteristics', {})
        tax = animal.get('taxonomy', {})
        scientific_name = tax.get('scientific_name')
        a_type = char.get('type')
        diet = char.get('diet')
        location = animal.get('locations', [None])[0]

        card_item_template = f"""
        <li class="cards__item">
          <div class="card__title">{name}</div>
          <p class="card__text">
              <strong>Scientific Name:</strong> <i>{scientific_name}</i><br/>
              <strong>Diet:</strong> {diet}<br/>
              <strong>Location:</strong> {location}<br/>
              <strong>Type:</strong> {a_type}<br/>
          </p>
        </li>
        """
        output_string += card_item_template

    return output_string


def read_html_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def write_html_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


def main():
    animal_data = serialize_animal()
    html_content = read_html_file('animals_template.html')
    html_content = html_content.replace('__REPLACE_ANIMALS_INFO__', animal_data)
    write_html_file('animals.html', html_content)


if __name__ == "__main__":
    main()