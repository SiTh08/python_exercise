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

def test_volume_cube():
    assert volume_cube(2) == 8

def test_volume_cube1():
    assert volume_cube(5) == 125

def test_volume_cube2():
    assert volume_cube(10) == 1000

def test_SA_cube():
    assert SA_cube(2) == 24

def test_SA_cube1():
    assert SA_cube(10) == 600

def test_constant():
    assert constant(3) == 24

def test_constant1():
    assert constant(8) == 64

def test_constant2():
    assert constant(20) == 160


