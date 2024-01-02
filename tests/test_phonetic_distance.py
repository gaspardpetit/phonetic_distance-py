"""Unit tests for phonetic_ditance"""
import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
# pylint: disable=import-error,wrong-import-position
from phonetic_distance import phonetic_distance

class TestPhoneticDistance(unittest.TestCase):
    """Unit test"""
    def test_phonetic_distance(self):
        """Unit test"""
        with open("tests/test_cases.txt", "r", encoding="utf-8") as f:
            for line in f:
                clean = line.split("#")[0].strip()
                if clean == "":
                    continue

                [lang, word_a, word_b, exp_score_lang, exp_score_any] = line.split()
                with self.subTest(input_string=word_a):
                    result = phonetic_distance(word_a, word_b, lang)
                    if result != int(exp_score_lang):
                        print(f"phonetic_distance('{word_a}', '{word_b}', '{lang}') = {result} " +
                                f"[expecting {exp_score_lang}]")
                        self.assertEqual(result, exp_score_lang)
                    result = phonetic_distance(word_a, word_b)
                    if result != int(exp_score_any):
                        print(f"phonetic_distance('{word_a}', '{word_b}') = {result} " +
                                f"[expecting {exp_score_any}]")
                        self.assertEqual(result, exp_score_any)


if __name__ == '__main__':
    unittest.main()
