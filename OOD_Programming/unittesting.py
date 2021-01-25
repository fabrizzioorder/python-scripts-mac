'''
Unittest Class

Piero Orderique
24 Jan 2021

For testing my data structures module and other self made classes
'''

import unittest
from datastructures import Dequeue

class TestDequeue(unittest.TestCase):

    # setUp called before every test
    def setUp(self) -> None:
        # Arrange
        self.d = Dequeue()

    # tearDown called after every test
    def tearDown(self) -> None:
        self.d = None

    def test_add1(self):
        # Arrange
        self.d.add("piero")
        self.d.add("fabrizzio")
        # Act
        first = self.d.first.data
        last = self.d.last.data
        # Assert
        self.assertEqual(first, "piero", "first OK")
        self.assertEqual(last, "fabrizzio", "second OK")

    def test_add_and_len(self):
        # Arrange
        self.d.add("piero")
        self.d.add("fabrizzio")
        self.d.add("orderique")
        # Act
        first = self.d.first.data
        last = self.d.last.data
        # Assert
        self.assertEqual(first, "piero", "first OK")
        self.assertEqual(last, "orderique", "second OK")
        self.assertEqual(3, len(self.d))

    def test_pop_and_len(self):
        self.d.add("piero")
        self.d.add("fab")
        self.d.add("orderique")
        self.d.pop_first()
        self.assertEqual(2, len(self.d))
        first = self.d.pop_first()
        last = self.d.pop_last()
        self.assertEqual(first.data, "fab")
        self.assertEqual(last.data, "orderique")

if __name__ == "__main__":
    print("\nTEST RESULTS")
    unittest.main()
