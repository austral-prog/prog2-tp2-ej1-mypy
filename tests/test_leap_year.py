import io
import unittest.mock
from src.leap_year import is_leap_year


class TP2LeapYearTest(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_2000(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="2000"):
            r1 = is_leap_year()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "El año 2000 es bisiesto")
            self.assertEqual(r1, True)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_2001(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="2001"):
            r2 = is_leap_year()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "El año 2001 no es bisiesto")
            self.assertEqual(r2, False)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_1700(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="1700"):
            r3 = is_leap_year()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "El año 1700 no es bisiesto")
            self.assertEqual(r3, False)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_100(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="100"):
            r4 = is_leap_year()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "El año 100 no es bisiesto")
            self.assertEqual(r4, False)


if __name__ == '__main__':
    unittest.main()