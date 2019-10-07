import pytest

from exercise_101 import *

def test_hello_human1():
    assert hello_human('Jefferson') == 'Hello Jefferson, you are a human'

def test_hello_human2():
    assert hello_human('Joana') == 'Hello Joana, you are a human'

def test_hello_human3():
    assert hello_human('Francis') == 'Hello Francis, you are a human'

def test_area_square():
    assert area_square(10) == 100

def test_area_square1():
    assert area_square(13) == 169

def test_area_square2():
    assert area_square(25) == 625

def test_area_triangle():
    assert area_triangle(10, 10) == 50

def test_area_triangle1():
    assert area_triangle(10, 13) == 65

def test_area_triangle2():
    assert area_triangle(20, 15) == 150
