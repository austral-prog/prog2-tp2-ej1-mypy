import io
import unittest.mock
from src.leap_year import leap_year


class TP2LeapYearTest(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_slice_advanced(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="2000"):
            r1 = leap_year()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "El año 2000 es bisiesto")
            self.assertEqual(r1, True)
        with unittest.mock.patch('builtins.input', return_value="2001"):
            r2 = leap_year()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[1], "El año 2001 no es bisiesto")
            self.assertEqual(r2, False)
        with unittest.mock.patch('builtins.input', return_value="1700"):
            r3 = leap_year()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[2], "El año 1700 no es bisiesto")
            self.assertEqual(r3, False)
        with unittest.mock.patch('builtins.input', return_value="100"):
            r4 = leap_year()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[3], "El año 100 no es bisiesto")
            self.assertEqual(r4, False)


if __name__ == '__main__':
    unittest.main()