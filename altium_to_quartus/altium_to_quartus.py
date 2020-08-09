import argparse
from collections import defaultdict

def func_name(input_file, u, output_file):
    with open(input_file, "r") as reader, open(output_file, "w+") as writer:
        big_dct = defaultdict(dict)
        for line in reader:
            small_dct = {}
            
            if line.startswith("NODENAME"):
                
                lst = list(line.rstrip("\n").rstrip("$").split(" "))
                lst = list(filter(None, lst))
                #print(lst)

                
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
        
        for key,value in big_dct.items():
            
            # print("key", key)
            # print("value", value)
            # print("keys", value.keys())
            # print("values", value.values())

            if not "_" in value.keys():
                if "_P" and "_N" in value.keys():
                    print("ok")
                else:
                    print(f"Net {key} belongs to a differential pair but has no corresponding negative or positive net.")
            
            # if "_P" in value.keys():
            #     net_name = key
            #     pin = value.values()[-1][-1]
            #     report = f"""set_location_assignment PIN_{pin} -to '{net_name}'"""
            #     print("report", report)
                #print(net_name)
                #report = f"""set_location_assignment PIN_{} -to '{}'"""
                #writer.write(report, "\n")


def create_corresponding_line(line):
    return line.split("_P$")[0]+"_N$"
    


def Main():
    args = parse_arguments()
    result = func_name(args.input_file, args.u, args.output)
    print(result)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", help="reference designator")
    parser.add_argument("-o", "--output", help="output result to a file")
    parser.add_argument("input_file", help="input file")

    args = parser.parse_args()
    return args

    
if __name__ == '__main__':
    Main()
