import optparse


def parse_commandline(func):

    """
    returns (files, test_mode) created from the command line arguments
    passed to pytddmon.
    """
    usage = "usage: %prog [options] [static file list]"
    version = "%prog " + '1.0.8'
    parser = optparse.OptionParser(usage=usage, version=version)
#     parser.add_option(
#         "--log-and-exit",
#         action="store_true",
#         default=False,
#         help='Run all tests, write the results to "pytddmon.log" and exit.')
#     parser.add_option(    options = parser.parse_args()

#         "--log-path",
#         help='Instead of writing to "pytddmon.log" in --log-and-exit, ' +
#              'write to LOG_PATH.')
    parser.add_option(
        "--gen-kata",
        help='Generate a stub unit test file appropriate for jump ' +
             'starting a kata')
#     parser.add_option(
#         "--no-pulse",
#         dest="pulse_disabled",
#         action="store_true",
#         default=False,
#         help='Disable the "heartbeating colorshift" of pytddmon.')
#     if not args:
#         args = "^[^\\.].*.py"  # If static file set not provided set default
#
    def wrapped_func(*args, **kwargs):
        options, cmd_args = parser.parse_args()

        return func(
            *args,
            **kwargs,
            cmd_args=cmd_args,
            # options.log_and_exit,
            # options.log_path,
            # options.pulse_disabled,
            kata_name=options.gen_kata)
    return wrapped_func


def kata_generator(kata_handler, kata_name):
    return (kata_name[0].isdigit() and kata_handler(None, 'Invalid Kata Name %s' % kata_name)) or kata_handler('test_' + kata_name.lower().replace(' ', '_') + '.py','''\
# coding: utf-8
import unittest
# Unit tests for kata '{0}'.

class {1}(unittest.TestCase):

    def test_something(self):
        self.assertTrue(True)

    def test_another_thing(self):
        self.assertEqual([1, 2], [x for x in range(1, 3)])

'''.format(kata_name, kata_name.title().replace(' ', '') + 'Tests'))


def main(kata_handler, cmd_args, kata_name):
    return kata_generator(kata_handler=kata_handler, kata_name=kata_name)


def kata_handler(file_name, file_content):
    return (file_name is None and print(file_content)) or write_file(file_name, file_content)


def write_file(file_name, file_content):
    with open(file_name, 'w') as outfile:
        outfile.write(file_content)

if __name__ == '__main__':
    parse_commandline(main)(kata_handler=write_file)