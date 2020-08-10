import sys
import argparse
from collections import defaultdict


def input_to_dict(input_file):    
    with open(input_file, "r") as reader:
        big_dct = defaultdict(dict)
        for line in reader:
            small_dct = {}

            if line.startswith("NODENAME"):
                # clean one line
                lst = list(line.rstrip("\n").rstrip("$").split(" "))
                lst = list(filter(None, lst))
                #print(lst)

                # clean next/corresponding line
                components_lst = next(iter(reader)).rstrip("\n").split(" ")
                components_lst = list(filter(None, components_lst))
                it = iter(components_lst)
                components_lst = list(zip(it, it))
                #print(components_lst)
                
                if lst[1].endswith("_P") or lst[1].endswith("_N"):
                    big_key = lst[1][:-2].rstrip(".")
                    small_key = lst[1][-2:]
                    #print(big_key)
                    #print(small_key)
                else:
                    big_key = lst[1]
                    small_key = "_"
                    #print(big_key)
                    #print(small_key)
                small_dct = big_dct[big_key]
                small_dct[small_key] = components_lst
        #print(big_dct)
    return big_dct


def corresponding_line_checker(dct):
    for net, small_dct in dct.items():
        if not "_" in small_dct.keys():
            if not "_P" in small_dct.keys() or not "_N" in small_dct.keys():
                print(f"Net {net} belongs to a differential pair but has no corresponding negative or positive counterpart.")
                sys.exit(1)


def ref_des_writer(dct, u, output_file):
    with open(output_file, "w+") as writer:
        for net, small_dct in dct.items():
            for item, comps in small_dct.items():
                for (comp, pin) in comps:
                    if comp == u:
                        net_ending_digits = extract_net_ending_digits(net)
                        non_digit_net_name = extract_net_name(net)
                        if "_" in net or "-" in net or "." in net:
                            if net_ending_digits != None:
                                if item == "_N":
                                    report = report = f"""set_location_assignment PIN_{pin} -to '{non_digit_net_name}[{net_ending_digits}](n)'\n"""
                                else:
                                    report = f"""set_location_assignment PIN_{pin} -to '{non_digit_net_name}[{net_ending_digits}]'\n"""
                            else:
                                report = f"""set_location_assignment PIN_{pin} -to '{net}'\n"""
                        else:
                            report = f"""set_location_assignment PIN_{pin} -to '{net}'\n"""
                        writer.write(report)
            

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


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", help="reference designator", default="U1")
    parser.add_argument("-o", "--output", help="output result to a file", default="result.qsf")
    parser.add_argument("input_file", help="input file")

    args = parser.parse_args()
    if args.output == "result.qsf":
        args.output = args.input_file.split(".")[0]+".qsf"

    return args


def Main():
    args = parse_arguments()
    dct = input_to_dict(args.input_file)
    corresponding_line_checker(dct)
    ref_des_writer(dct, args.u, args.output)

    
if __name__ == '__main__':
    Main()
