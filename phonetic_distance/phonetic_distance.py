"""Computes a distance score between two words phonetically"""
from itertools import product
from phonetic_fr import phonetic as phonetic_fr
from metaphone import doublemetaphone
from Levenshtein import distance
import cutlet

katsu = cutlet.Cutlet()

def normalize(word, lang):
    if lang == "ja" or lang is None:
        normalized = katsu.slug(word)
        if normalized:
            return normalized

    return word

PHONETIC = {
    "fr": lambda word : [phonetic_fr(word)],
    "ja": lambda word : [phonetic_fr(word)],
    "default": lambda word : [w for w in doublemetaphone(word) if w],
}

def phonetic(word:str, lang:str) -> list:
    """
    Convert the input word to its phonetic representation in the specified language.

    Parameters:
    - word (str): The input word to be converted to its phonetic representation.
    - lang (str): The language code indicating the phonetic representation to use.

    Returns:
    - list: A list containing the phonetic representation of the input word.

    If the specified language is not supported, the default phonetic representation will be used.
    """
    word = normalize(word, lang)
    if lang in PHONETIC:
        return PHONETIC[lang](word)

    return PHONETIC['default'](word)

def phonetic_distance_any(word_a:str, word_b:str):
    """
    Calculate the phonetic distance between two words using various phonetic representation methods.

    Parameters:
    - word_a (str): The first word for calculating phonetic distance.
    - word_b (str): The second word for calculating phonetic distance.

    Returns:
    - int: The phonetic distance between the two words. Returns 0 if the words are 
    phonetically identical.

    This function iterates through different phonetic representation methods and calculates the
    minimum phonetic distance between the two input words. If the minimum distance is 0, it means
    the words are phonetically identical, and 0 is returned.
    """
    word_a = normalize(word_a, None)
    word_b = normalize(word_b, None)
    best_score = None
    for method in set(["fr", "default"]):
        phone_a = PHONETIC[method](word_a)
        phone_b = PHONETIC[method](word_b)
        if len(phone_a) > 0 and len(phone_b)  > 0:
            score = min([distance(a, b) for a, b in product(phone_a, phone_b)])
            if best_score is None or score < best_score:
                best_score = score
                if best_score == 0:
                    return best_score
    return best_score

def phonetic_distance(word_a:str, word_b:str, lang:str = None):
    """
    Calculate the phonetic distance between two words using a specified phonetic 
    representation method or any available method.

    Parameters:
    - word_a (str): The first word for calculating phonetic distance.
    - word_b (str): The second word for calculating phonetic distance.
    - lang (str, optional): The language code indicating the specific phonetic 
    representation to use. If not provided (default), the function uses any available 
    phonetic method.

    Returns:
    - int: The phonetic distance between the two words. Returns 0 if the words are 
    phonetically identical.

    If the language code is specified (lang parameter is not None), the function 
    calculates the phonetic distance between the two words using the specified 
    phonetic representation method. If lang is not provided (None), the function 
    uses any available phonetic representation method and calculates the minimum 
    phonetic distance.
    """
    if lang is None:
        return phonetic_distance_any(word_a, word_b)
    else:
        word_a = normalize(word_a, lang)
        word_b = normalize(word_b, lang)
        phone_a = phonetic(word_a, lang)
        phone_b = phonetic(word_b, lang)
        if len(phone_a) > 0 and len(phone_b)  > 0:
            return min([distance(a, b) for a, b in product(phone_a, phone_b)])
        else:
            return None

def main():
    """Samples"""
    lang = "en"
    word_a = "Gilles"
    word_b = "Jill"

    print(phonetic_distance("Día", "Noche", "es"))

    print(phonetic(word_a, lang))
    print(phonetic(word_b, lang))
    print(phonetic_distance(word_a, word_b, lang))
    print(phonetic_distance(word_a, word_b))

if __name__ == '__main__':
    main()
