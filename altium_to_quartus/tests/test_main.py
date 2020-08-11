import sys
import unittest
import yaml
from unittest.mock import patch
from parameterized import parameterized, param
from altium_to_quartus import parse_arguments, a_to_q
from os.path import join
from os import walk

class TestInputArgs(unittest.TestCase):

    @parameterized.expand([
        (['app_name', '-u', 'U3', '-o', 'output.qsf', 'input.net'], 'input.net', 'output.qsf', 'U3'),
        (['app_name', '-o', 'output.qsf', '-u', 'U3', 'input.net'], 'input.net', 'output.qsf', 'U3'),
        (['app_name', 'input.net'], 'input.net', 'input.qsf', 'U1'),
        (['app_name', '-u', 'U3', 'input.net'], 'input.net', 'input.qsf', 'U3'),
        (['app_name', '-o', 'output.qsf', 'input.net'], 'input.net', 'output.qsf', 'U1'),
    ])
    def test_args_parser(self, test_args, input_name, output_name, refdes):
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
            self.assertEquals(args.input_file, input_name)
            self.assertEquals(args.output, output_name)
            self.assertEquals(args.u, refdes)


def files_provider(path):
    filenames = list()
    for _ , _ , names in walk(path):
        filenames.extend(names)
        break

    for filename in filenames:
        if filename.startswith('correct_') and filename.endswith('.in'):
            yield (filename, path)

class TestFunctionality(unittest.TestCase):

    @parameterized.expand(files_provider('tests/cases/'))
    def test_case(self, *params):
        input_filename, path = params
        expected_filename = input_filename[:-3] + '.out'
        input_path = join(path, input_filename)
        expected_path = join(path, expected_filename)

        with open(input_path) as input_data, open (expected_path) as expected_data:
            self.assertMultiLineEqual("".join(list(a_to_q(input_data, 'U3'))), expected_data.read())


if __name__ == "__main__":
    unittest.main()