import sys
import unittest
from unittest.mock import patch
from parameterized import parameterized
from altium_to_quartus import parse_arguments

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


if __name__ == "__main__":
    unittest.main()