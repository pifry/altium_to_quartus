import sys

def parse_args(*args):
    input_name = args[-1]
    return (input_name, 0, 0)

if __name__ == '__main__':
    input_file_name, output_file_name, ref_des = parse_args(*sys.argv)