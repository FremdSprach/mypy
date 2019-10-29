"""
A simple test with py.test.
"""
import pytest


def test_demo():
    assert 'UPPER'.isupper()  # passed.
    assert 'UPPER'.islower()  # failed.


def main():
    pytest.main()


if __name__ == '__main__':
    main()
