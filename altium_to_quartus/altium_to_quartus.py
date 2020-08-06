import argparse

def func_name(input_file, u, output_file):
    with open(input_file, "r") as reader, open(output_file, "w+") as writer:
        for line in reader:
            if line.startswith("NODENAME"):
                lst = list(line.rstrip("\n").split(" "))
                lst = list(filter(None, lst))
                next_lst = next(iter(reader)).rstrip("\n").split(" ")
                next_lst = list(filter(None, next_lst))
                lst.extend(next_lst)
                writer.write(str(" ".join(lst) + "\n"))


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", help="reference designator")
    parser.add_argument("-o", "--output", help="output result to a file")
    parser.add_argument("input_file", help="input file")

    args = parser.parse_args()

    result = func_name(args.input_file, args.u, args.output)
    print(result)

if __name__ == '__main__':
    Main()
