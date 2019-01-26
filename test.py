import unittest

from parser import parse


class TestParse(unittest.TestCase):
    def test_parsed_lines(self):
        """
        Test that it parse a csv file
        """
        file = "data.csv"
        result = parse(file)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
