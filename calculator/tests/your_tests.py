#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!

def test_add():
	result = run("5", "+", "3")
	assert result == "8"

def test_multiply():
	result = run("4", "*", "2")
	assert result == "8"
