import argparse
from collections import defaultdict


def func_name(input_file, u, output_file): 
    # transform input file into nested dicts
    dct = input_to_dict(input_file)
    # checking corresponding lines
    corresponding_line_checker(dct)
    # generating output file
    ref_des_writer(dct, u, output_file)
    print("a kuku")



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
                    big_key = lst[1][:-2]
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
            if not "_P" and not "_N" in item.keys():
                print(f"Net {net} belongs to a differential pair but has no corresponding negative or positive counterpart.")
            return None


def ref_des_writer(dct, u, output_file):
    print("my u is ", u)
    with open(output_file, "w+") as writer:
        for net, small_dct in dct.items():
            for item, comps in small_dct.items():
                for (comp, pin) in comps:
                    if comp == u:
                        net_ending_digits = extract_net_ending_digits(net)
                        if net_ending_digits != None:
                            report = f"""set_location_assignment PIN_{pin} -to '{net} [{net_ending_digits}]'\n"""
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


        

            # if not "_" in value.keys():
            #     if "_P" and "_N" in value.keys():
            #         print("ok")
            #     else:
            #         print(f"Net {key} belongs to a differential pair but has no corresponding negative or positive net.")
            


            # if "_P" in value.keys():
            #     net_name = key
            #     pin = value.values()[-1][-1]
            #     report = f"""set_location_assignment PIN_{pin} -to '{net_name}'"""
            #     print("report", report)
                #print(net_name)
                #report = f"""set_location_assignment PIN_{} -to '{}'"""
                #writer.write(report, "\n")

#with open(output_file, "w+") as writer

# def create_corresponding_line(line):
#     return line.split("_P$")[0]+"_N$"
    



def Main():
    args = parse_arguments()
    result = func_name(args.input_file, args.u, args.output)
    print(result)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", help="reference designator", default="U1")
    parser.add_argument("-o", "--output", help="output result to a file", default="result.qsf")
    parser.add_argument("input_file", help="input file")

    args = parser.parse_args()
    return args

    
if __name__ == '__main__':
    Main()
