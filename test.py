import unittest
import random
import string
from parser import parse


class TestCsvParser(unittest.TestCase):

    def test_parse_right_csv_file(self):
        """
        Test that parse a csv file with all lines completed
        """
        file = "users_data.txt"
        result = parse(file)
        self.assertEqual(result.processed_rows, 2)
        self.assertEqual(result.inserted_rows, 2)

    def test_parse_wrong_csv_file(self):
        """
        Test that parse a csv file with uncompleted lines
        """
        file = "wrong_users_data.txt"
        result = parse(file)
        self.assertEqual(result.processed_rows, 2)
        self.assertEqual(result.inserted_rows, 1)

    def test_parse_non_existent_csv_file(self):
        """
        Test that tries to parse a non existent csv file
        """
        random_filename = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(8)])
        filename = "%s.txt" % random_filename
        result = parse(filename)
        self.assertEqual(result.inserted_rows, 0)
        self.assertEqual(result.processed_rows, 0)
        self.assertNotEqual(result.error, None)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCsvParser)
    unittest.TextTestRunner(verbosity=2).run(suite)
