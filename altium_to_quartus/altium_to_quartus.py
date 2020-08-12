import sys
import argparse
from collections import defaultdict

def input_to_dict(input_data):    
    big_dct = defaultdict(dict)

    for line in input_data:
        small_dct = {}

        if line.startswith("NODENAME"):
            lst = list(line.rstrip("\n").rstrip("$").split(" "))
            lst = list(filter(None, lst))

            components_lst = next(iter(input_data)).rstrip("\n").split(" ")
            components_lst = list(filter(None, components_lst))
            it = iter(components_lst)
            components_lst = list(zip(it, it))
            
            if lst[1].endswith("_P") or lst[1].endswith("_N"):
                big_key = lst[1][:-2].rstrip(".")
                small_key = lst[1][-2:]
            else:
                big_key = lst[1]
                small_key = "_"
            small_dct = big_dct[big_key]
            small_dct[small_key] = components_lst
    #print(big_dct)
    return big_dct


def check_corresponding_line(dct):
    count = 0
    for net, small_dct in dct.items():
        if not "_" in small_dct.keys():
            if not "_P" in small_dct.keys() or not "_N" in small_dct.keys():
                count += 1
                print(f"Net {net} belongs to a differential pair but has no corresponding negative or positive counterpart.")
    if count !=0:
        sys.exit(1)


def extract_net_ending_digits(net_name):
    import re
    net_ending_regex = re.compile(r'(\d+)$')
    mo = net_ending_regex.search(net_name)
    if mo:
        return mo.group()
    else:
        return None


def extract_net_name(net_name):
    import re
    if "_" in net_name or "-" in net_name or ".":
        result = re.split(r'(\d+)$', net_name, 1)[0].rstrip("_-.")
    else:
        result = net_name
    return result


def generate_output(dct, u):
    for net, small_dct in dct.items():
        for item, comps in small_dct.items():
            for (comp, pin) in comps:
                if comp == u:
                    net_ending_digits = extract_net_ending_digits(net)
                    non_digit_net_name = extract_net_name(net)
                    if "_" in net or "-" in net or "." in net:
                        if net_ending_digits != None:
                            if item == "_N":
                                report = f"""set_location_assignment PIN_{pin} -to \"{non_digit_net_name}[{net_ending_digits}](n)\"\n"""
                            else:
                                report = f"""set_location_assignment PIN_{pin} -to \"{non_digit_net_name}[{net_ending_digits}]\"\n"""
                        else:
                            if item == "_N":
                                report = f"""set_location_assignment PIN_{pin} -to \"{net}(n)\"\n"""
                            else:
                                report = f"""set_location_assignment PIN_{pin} -to \"{net}\"\n"""
                    else:
                        if item == "_N":
                                report = f"""set_location_assignment PIN_{pin} -to \"{net}(n)\"\n"""
                        else:
                            report = f"""set_location_assignment PIN_{pin} -to \"{net}\"\n"""
                    yield report


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", help="reference designator", default="U1")
    parser.add_argument("-o", "--output", help="output result to a file", default=None)
    parser.add_argument("input_file", help="input file")

    args = parser.parse_args()
    if args.output == None:
        args.output = args.input_file.split(".")[0]+".qsf"
    return (args.input_file, args.output, args.u)

def a_to_q(input_data, ref_des):
    dct = input_to_dict(input_data)
    check_corresponding_line(dct)
    for line in generate_output(dct, ref_des):
        yield line


if __name__ == '__main__':
    input_file_path, output_file_path, ref_des = parse_arguments()

    with open(input_file_path, 'r') as input_file, open(output_file_path,'w') as output_file:
        for line in a_to_q(input_file, ref_des):
            output_file.write(line)
