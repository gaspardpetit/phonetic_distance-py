[![Pylint](https://github.com/gaspardpetit/phonetic_distance-py/actions/workflows/pylint.yml/badge.svg)](https://github.com/gaspardpetit/phonetic_distance-py/actions/workflows/pylint.yml)[![Python package](https://github.com/gaspardpetit/phonetic_distance-py/actions/workflows/python-package.yml/badge.svg)](https://github.com/gaspardpetit/phonetic_distance-py/actions/workflows/python-package.yml)
[![Python versions](https://img.shields.io/pypi/pyversions/phonetic_distance.svg)](https://pypi.org/project/phonetic_distance/)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# phonetic_distance
Computes a similarity score based on how words sound when pronounced.

## Purpose
`phonetic_distance` uses a Soundex phonetic algorithms to compute a similarity score between two words. The language can be provided. When not provided, the returned score will be the lowest across all supported languages.

## How to install
```{bash}
pip install phonetic_distance
```
or

```{bash}
pip install git+https://github.com/gaspardpetit/phonetic_distance-py.git
```

## Usage in shell
```{bash}
phonetic_distance Gilles Jill
phonetic_distance Gilles Bill
phonetic_distance Gilles Robert
```

Prints:
```{bash}
0
1
4
```

## Usage in Python
```{py}
from phonphonetic_distance import phonetic_distance

print(phonetic_distance("Gilles", "Jill"))
print(phonetic_distance("Gilles", "Bill"))
print(phonetic_distance("Gilles", "Robert"))
```

Prints

```
0
1
4
```

## Language support
The objective of this project is to support as many languages as possible. Feel free to reach out if you can contribute. The main languages I will personally attempt to support are English, French, Spanish, Italian and Japanese.

## License

`phonetic_distance` is released under the MIT license. Feel free to use, modify, and distribute it according to the terms of the license.

## Credits

This project depends on the following other projects:
- [DoubleMetaphone](https://pypi.org/project/DoubleMetaphone/)
- [phonetic_fr](https://github.com/gaspardpetit/phonetic_fr-py)

