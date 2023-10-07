import unittest
import prog.py

class TestProgram(unittest.TestCase):
    def test_new_string(self):
        a = "Hello"
        b = "World"
        c = "!"
        expected_result = "Hello World!"
        new_string = string_1.concatenate_strings(a, b, c)
        self.assertEqual(new_string, expected_result)

if __name__ == '__main__':
    unittest.main()
