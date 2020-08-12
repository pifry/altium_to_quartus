import argparse

def parse_arguments():
    # Implement function here and return values according 
    # to the following example:
    return ('input.net', 'output.qsf', 'U3')

def a_to_q(input_data, ref_des):
    # Following implementation is a fake whose sole purpose 
    # is to channel data from input to output.
    content = list()
    for line in input_data:
        content.append(line)

    for line in content:
        yield line

if __name__ == '__main__':
    input_file_path, output_file_path, ref_des = parse_arguments()

    with open(input_file_path, 'r') as input_file, open(output_file_path,'w') as output_file:
        for line in a_to_q(input_file, ref_des):
            output_file.write(line)
    