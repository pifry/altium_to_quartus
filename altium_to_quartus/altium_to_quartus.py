import argparse

def parse_arguments():
    class Ret:
        def __init__(self):
            self.input_file = ""
            self.output = ""
            self.u = ""
    return Ret()

def a_to_q(input_data, ref_des):
    content = list()
    for line in input_data:
        content.append(line)

    for line in content:
        yield line

if __name__ == '__main__':
    parse_arguments()

    input_data = ['pierwszy\n', 'drugi\n', 'trzeci\n']
    with open('tmp.txt','w') as f:
        for line in a_to_q(input_data, 'U3'):
            f.write(line)
    