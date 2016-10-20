import pytddmon2
import pytest


@pytest.mark.parametrize('input_kata_name', ('test1','test2', '123123123',' test three', '123123443.txt', ' ',))
def test_gen_kata_args(input_kata_name):
    # Setup
    pytddmon2.optparse.sys.argv = ['pytddmon2.py', '--gen-kata', input_kata_name]
    # Exercise & Verify
    assert pytddmon2.parse_commandline(lambda cmd_args, kata_name: input_kata_name == kata_name)()
    # Teardown
    pytddmon2.optparse.sys.argv = list()
