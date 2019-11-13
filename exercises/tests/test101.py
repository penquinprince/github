import unittest
import ast
import inspect
from exercises.python101 import *


def contains_explicit_for(f):
    return


# No need to change these tests.
class Test101(unittest.TestCase):

    def setUp(self):
        pass

    def test_101(self):
        if not foo():
            self.fail("The method foo() should return True!")


class TestEven(unittest.TestCase):

    def setUp(self):
        pass

    def test_even_steven_for(self):
        if not (any(isinstance(node, ast.For) for node in ast.walk(ast.parse(inspect.getsource(even_steven))))):
            self.fail("The method even_steven() should contain a for loop!")


class TestConcatenadd(unittest.TestCase):

    def setUp(self):
        pass

    def test_plus(self):
        a = 5
        b = 8
        for a, b, c in [
            (5, 8, 13),
            (5.5, 8.5, 14.),
            ("ab", "cd", "abcd"),
        ]:
            result = concatenadd(a, b)
            if not result == c:
                self.fail(
                    "The method Concatenadd failed with arguments {} and {}. Should have returned {}, but returned {}".format(
                        a, b, c, result))


class TestCfColor(unittest.TestCase):
    def setUp(self):
        pass

    def test_cf_color(self):
        for frogs, clutch, color in [(1, -1, "blue"), (1, 0.5, "green"), (-3, -1.5, "white"), (1, -0.5, "blue"),
                                     (-1, -0.5, "red"), (-1, -1.5, "black")]:
            result = cf_color(frogs, clutch)
            if result != color:
                self.fail(
                    "The method cf_color failed, with {} and {} it should have returned {}, but it returned {}.".format(
                        frogs, clutch, color, result))


class TestCollatz(unittest.TestCase):

    def setUp(self):
        pass

    def test_collatz(self):
        for x, y in [(5, 5), (7, 16), (19, 20)]:
            result = collatz(x)
            if result != y:
                self.fail(
                    "The method collatz failed, with {}, it should have returned {}, but it returned {}.".format(x, y,
                                                                                                                 result))


class TestTypedCollatz(unittest.TestCase):

    def setUp(self):
        pass

    def test_typed_collatz(self):
        for x, y in [(5, 5), (7.5, 16), (-2, None), ("Ffdfd", None)]:
            result = collatz(x)
            if result != y:
                self.fail(
                    "The method collatz failed, with {}, it should have returned {}, but it returned {}.".format(x, y,
                                                                                                                 result))
class TestExtendE(unittest.TestCase):

    def setUp(self):
        pass

    def test_extend_e(self):
        for x, y in [("Hello", "Heelloe"),("This hovercraft is full of eels.", "Thies hoeveercraeft ies fuell oef eeeels.")]:
            result = extend_e(x)
            if result != y:
                self.fail("The method 'extend_e' failed, with '{}', it should have returned '{}', but it returned '{}'.".format(x,
                                                                                                                    y,result))
class TestReply2(unittest.TestCase):

    def setUp(self):
        pass

    def test_reply_2(self):
        for x, y in [("Yes, sure is", "No! Ooooh! Yeees, sueree ies"),("What do you mean?", "None of your business. ")]:
            result = reply2argument(x)
            if result != y:
                self.fail("The method 'reply2argument' failed, with '{}', it should have returned '{}', but it returned '{}'.".format(x, y,result))


if __name__ == "__main__":
    unittest.main()
