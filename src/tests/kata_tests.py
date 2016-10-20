import pytddmon2
import pytest


@pytest.mark.parametrize('input_kata_name, expected_kata_filename, expected_kata_content', (
        ('test1', 'test_test1.py', '''\
# coding: utf-8
import unittest
# Unit tests for kata 'test1'.

class Test1Tests(unittest.TestCase):

    def test_something(self):
        self.assertTrue(True)

    def test_another_thing(self):
        self.assertEqual([1, 2], [x for x in range(1, 3)])

'''),
        ('test2', 'test_test2.py','''\
# coding: utf-8
import unittest
# Unit tests for kata 'test2'.

class Test2Tests(unittest.TestCase):

    def test_something(self):
        self.assertTrue(True)

    def test_another_thing(self):
        self.assertEqual([1, 2], [x for x in range(1, 3)])

'''),
        ('123123123', None, 'Invalid Kata Name 123123123'),
        ('test three', 'test_test_three.py','''\
# coding: utf-8
import unittest
# Unit tests for kata 'test three'.

class TestThreeTests(unittest.TestCase):

    def test_something(self):
        self.assertTrue(True)

    def test_another_thing(self):
        self.assertEqual([1, 2], [x for x in range(1, 3)])

'''),
        ('123123443.txt', None, 'Invalid Kata Name 123123443.txt'),
        (' ', 'test__.py','''\
# coding: utf-8
import unittest
# Unit tests for kata ' '.

class Tests(unittest.TestCase):

    def test_something(self):
        self.assertTrue(True)

    def test_another_thing(self):
        self.assertEqual([1, 2], [x for x in range(1, 3)])

''')))
def test_kata_gen(input_kata_name, expected_kata_filename, expected_kata_content):
    # Exercise & Verify
    assert pytddmon2.kata_generator(kata_handler=lambda kata_filename, kata_content:
    kata_filename == expected_kata_filename and kata_content == expected_kata_content,
                                    kata_name=input_kata_name)