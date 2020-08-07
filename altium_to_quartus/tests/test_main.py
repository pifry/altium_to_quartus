import sys
import unittest
from unittest.mock import patch
from altium_to_quartus import parse_arguments

class TestInputArgs(unittest.TestCase):

    def test_full_input(self):
        test_args = ['app_name', '-u', 'U3', '-o', 'output.qsv', 'input.net']
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
            self.assertEquals(args.input_file,'input.net')
            self.assertEquals(args.output,'output.qsv')
            self.assertEquals(args.u,'U3')

    def test_full_input_reversed(self):
        test_args = ['app_name', '-o', 'output.qsv', '-u', 'U3', 'input.net']
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
            self.assertEquals(args.input_file,'input.net')
            self.assertEquals(args.output,'output.qsv')
            self.assertEquals(args.u,'U3')
    
    def test_default_args(self):
        test_args = ['app_name', 'input.net']
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
            self.assertEquals(args.input_file,'input.net')
            self.assertEquals(args.output,'input.qsv')
            self.assertEquals(args.u,'U1')

    def test_specific_refdes(self):
        test_args = ['app_name', '-u', 'U3', 'input.net']
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
            self.assertEquals(args.input_file,'input.net')
            self.assertEquals(args.output,'input.qsv')
            self.assertEquals(args.u,'U3')

    def test_specific_output_name(self):
        test_args = ['app_name', '-o', 'output.qsv', 'input.net']
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
            self.assertEquals(args.input_file,'input.net')
            self.assertEquals(args.output,'output.qsv')
            self.assertEquals(args.u,'U1')

if __name__ == "__main__":
    unittest.main()