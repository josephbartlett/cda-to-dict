# cda_to_dict.py

`cda_to_dict.py` is a Python script designed to convert a Clinical Document Architecture (CDA) XML file into a Python dictionary structure. This allows for easy manipulation, analysis, and processing of CDA documents in a format that is more convenient for Python applications.

## Features

- Converts a CDA XML file to a nested dictionary representation.
- Strips XML namespaces for simpler access.
- Handles XML attributes and text content.
- Ignores comment nodes in the XML.

## Requirements

- Python 3.x
- lxml library

## Installation

Install the required dependencies using pip:

```bash
pip install lxml
```

## Usage

To use the script, run it from the command line with the path to the CDA XML file as an argument:

```bash
python cda_to_dict.py <cda_file>
```

### Example

Suppose you have a CDA XML file named `example_cda.xml`. You can convert it to a dictionary by running:

```bash
python cda_to_dict.py example_cda.xml
```

The script will output the dictionary representation of the CDA file.

### Programmatic Use

You can also use the `cda_to_dict` function in your own Python projects:

```python
from cda_to_dict import cda_to_dict

cda_file = "example_cda.xml"
cda_dict = cda_to_dict(cda_file)
print(cda_dict)
```

## Function Details

### `cda_to_dict(cda_file)`

**Parameters:**
- `cda_file` (str): The path to the CDA XML file.

**Returns:**
- A Python dictionary representing the structure and content of the CDA XML file.

### Key Features:
- Strips XML namespaces for easier access to tags.
- Converts attributes and text nodes into dictionary entries.
- Collapses child elements into nested dictionaries.

## Development and Contribution

Contributions are welcome! If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request on the project repository.

### Running Tests

Ensure you have test CDA XML files available and run the script to verify its output:

```bash
python cda_to_dict.py test_file.xml
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.