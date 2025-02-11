# Linked List Implementation in Python

This repository contains a Python implementation of a linked list that supports different types:

- **Singly Regular** (Linear singly linked list)
- **Doubly Regular** (Linear doubly linked list)
- **Singly Circular** (Circular singly linked list)
- **Doubly Circular** (Circular doubly linked list)

## Features

- ✅ Supports different types of linked lists
- ✅ Allows adding elements dynamically
- ✅ Generates and prints the linked list structure based on the selected type

## Installation

No installation required. Just clone the repository and run the script using Python.

```sh
git clone https://github.com/yourusername/linked-list-python.git
cd linked-list-python
python linked_list.py
```

## Usage

### Initializing a Linked List

```python
from linked_list import linkedList

# Create a linked list
ll = linkedList()
```

### Setting the Type of Linked List

```python
ll.set("doubly circular")  # Options: "singly regular", "doubly regular", "singly circular", "doubly circular"
```

### Adding Elements

```python
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
```

### Output the Linked List

```python
ll.output()
```

This will print the linked list representation based on the selected type.

## Example Output

For a **Doubly Circular** linked list with elements `[1, 2, 3, 4]`, the output will be:

```sh
[[4, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 1]]
```

## Contributing

Feel free to fork this repository and submit pull requests for improvements or additional features.

## License

This project is licensed under the MIT License.

