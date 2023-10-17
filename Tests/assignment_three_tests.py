# Eva D
# 10/16/2023
# unit test for assignment 3

import unittest
import assignment_three


class MyTestCase(unittest.TestCase):
    def test_surface_area_calculation(self):
        self.assertEqual(184, assignment_three.calc_surface_area_of_prism(5,4,8))

    def test_surface_area_calculation(self):
        self.assertEqual(150, assignment_three.calc_surface_area_of_prism(4,3,9))

    def test_final_surface_area_output(self):
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            assignment_three.print_answer(184)
            output = out.getvalue().strip()
            assert output == "The surface area of the prism is 184"
        finally:
            sys.standout = saved_stdout

if __name__ == '__main__':
    unittest.main()
