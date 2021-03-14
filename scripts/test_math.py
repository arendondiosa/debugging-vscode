import nose

from math_methods import add, divide
from unittest import TestCase


class TestMathMethods(TestCase):
    def test_add_integers(self):
        assert add(5, 3) == 8

    def test_add_integers_zero(self):
        assert add(3, 0) == 3

    def test_add_floats(self):
        assert add(1.5, 2.5) == 4

    def test_add_strings(self):
        nose.tools.assert_raises(AssertionError, add, "paul", "carol")

    def test_divide_integers_even(self):
        assert divide(2, 10) == 0.2

    def test_divide_integers_repetant(self):
        nose.tools.assert_almost_equal(divide(1, 3), 0.33333333, 7)
