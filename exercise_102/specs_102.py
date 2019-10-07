import pytest

from excercise_102 import *

def test_full_name1():
    assert full_name('Jefferson', 'Yunn') == 'Jefferson Yunn'

def test_full_name2():
    assert full_name('Andreia', 'Morales') == 'Andreia Morales'

def test_calculator_sum():
    assert calculator_sum(2, 4) == 6

def test_calculator_sum2():
    assert calculator_sum(10, 44) == 54

def test_calculator_sum3():
    assert calculator_sum(2, 4) == 6

def test_calculator_sum4():
    assert calculator_sum(2, 44) == 46

def test_calculator_subtract():
    assert calculator_subtract(20, 4) == 16

def test_calculator_subtract2():
    assert calculator_subtract(10, 4) == 6

def test_calculator_subtract3():
    assert calculator_subtract(20, 4) == 16

def test_calculator_subtract4():
    assert calculator_subtract(2, 44) == -42

def test_calculator_multiply():
    assert calculator_multiply(20, 4) == 80

def test_calculator_multiply2():
    assert calculator_multiply(10, 4) == 40

def test_calculator_multiply3():
    assert calculator_multiply(22, 4) == 88

def test_calculator_multiply4():
    assert calculator_multiply(2, 44) == 88

def test_area_square():
    assert area_square(10) == 100

def test_area_square1():
    assert area_square(13) == 169

def test_area_triangle():
    assert area_triangle(10, 10) == 50

def test_area_triangle2():
    assert area_triangle(10, 13) == 65
