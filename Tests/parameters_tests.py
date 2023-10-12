import unittest
import addition


class MyTestCase(unittest.TestCase):
    def test_addition_smaller_first(self):
        """
        You will use this function as a template for your own tests. You don't need to know what most of this means
        for right now, but the important thing is to change two lines: the addition.add_two() and the assert output
        lines. Everything else can stay the same.
        :return:
        """
        import sys
        from io import StringIO

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            addition.add_two(2, 4)
            output = out.getvalue().strip()
            assert output == "The sum of 2 and 4 is 6"
        finally:
            sys.stdout = saved_stdout

    def test_addition_larger_first(self):
        import sys
        from io import StringIO

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            addition.add_two(12, 9)
            output = out.getvalue().strip()
            assert output == "The sum of 12 and 9 is 21"
        finally:
            sys.stdout = saved_stdout

    def test_adding_one_negative(self):
        """
        Delete the word "pass" and write a test that will make sure your function works when adding a positive
        and a negative number
        :return: none
        """
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            addition.add_two(-10,9)
            output = out.getvalue().strip()
            assert output == "The sum of -10 and 9 is -1"
        finally:
            sys.standout = saved_stdout


    def test_adding_two_negatives(self):
        """
        Delete the word "pass" and write a test that will make sure your function works when adding two
        negative numbers.
        :return: none
        """
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            addition.add_two(-10, -10)
            output = out.getvalue().strip()
            assert output == "The sum of -10 and -10 is -20"
        finally:
            sys.standout = saved_stdout

    def test_volume_of_cone_with_no_height(self):
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            addition.volume_of_cone(10, 0)
            output = out.getvalue().strip()
            assert output == "The volume of a cone with a height of 0 cannot be calculated"
        finally:
            sys.standout = saved_stdout

    def test_volume_of_cone_with_multiples_a(self):
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            addition.volume_of_cone(10, 3)
            output = out.getvalue().strip()
            assert output == "The volume of a cone with a radius of 10 and a height of 3 is 314.0"
        finally:
            sys.standout = saved_stdout

    def test_volume_of_cone_with_multiples_b(self):
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            addition.volume_of_cone(20, 9)
            output = out.getvalue().strip()
            assert output == "The volume of a cone with a radius of 20 and a height of 9 is 3768.0"
        finally:
            sys.standout = saved_stdout


if __name__ == '__main__':
    unittest.main()
