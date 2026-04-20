#!/usr/bin/env python3
from calculator_adapter import run

def test_add():
    print("TEST RUN: addition")
    result = run("5", "+", "3")
    assert result == "8"

def test_multiply():
    print("TEST RUN: multiplication")
    result = run("4", "*", "2")
    assert result == "8"

if __name__ == "__main__":
    test_add()
    test_multiply()
