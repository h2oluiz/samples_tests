#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest


def test_excetion(name):
    if name != "Yana":
        raise Exception("Invalid User")
    else:
        return "Username is properly set"


def test_username_exception():
    """test that exception is raised for invalid username"""
    with pytest.raises(Exception):
        assert test_excetion("Yana")
    assert str(e.value) == "Username is properly set"


if __name__ == "__main__":
    pytest.main([__file__, "-k", "test_", "-v", "-s"])


# ---------------------------------------------------------------------------------------------
import pytest


def divide(a, b):
    if b == 0:
        return None
    return a / b


def test_zero_division():
    with pytest.raises(ValueError) as e:
        divide(0, 0)
    assert str(e.value) == 'Cannot divide by Zero'


import pytest


def test_ex():
    with pytest.raises(Exception) as e:
        raise Exception('blabla')
    assert 'blabla' in str(e)


def dummy_function():
    try:
        g = 1 / 0
    except Exception as e:
        raise Exception("There is an error: {}".format(e))


def test_dummy_function():
    with pytest.raises(ValueError) as e:
        dummy_function()
    print('==================================')
    print(e)
    assert str(e.value) == True


with pytest.raises(ValueError) as e:
    dummy_function()
assert str(e.value) == True
