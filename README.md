Altium to Quartus netlist converter  
===================================
![tests](https://github.com/pifry/altium_to_quartus/workflows/Python%20application/badge.svg)
The tool is made as a part of an atomatic toolchain linking [Altium Designer](https://www.altium.com/) project to [Quartus Prime](https://www.intel.pl/content/www/pl/pl/software/programmable/quartus-prime/overview.html) project. The goal is to convert netlist names connected to FPGA in Altium Designer to Quartus Pin declaration in qsf file.

## Usage:

`altium_to_quartus -u U3 -o result.qsf input.net` 

This should generate new result.qsf from input.net file. For the lines from input.net, that looks like this:

```
NODENAME LVDS_TOP_DATA.30_P$
    J1        79  U3      AH22
NODENAME LVDS_TOP_DATA.30_N$
    J1        79  U3      AH21
```

the lines below shoud be generated and saved into the result file:

```
set_location_assignment PIN_AH22 -to "LVDS_TOP_DATA[30]"
set_location_assignment PIN_AH21 -to "LVDS_TOP_DATA[30](n)"
```

Only lines with U3 should be considered as specyfied in `-u U3` parameter. 

The program shoud check whether every line in source file that ends with _P have corresponding line, with the same name, ending with _N. If not it shoud return non zero result, print missing nets names and do not generate any output files. For example:

```
Net LVDS_TOP_DATA.33_P belongs to a differential pair but has no it's corresponding negative net.
```
Below are examples of lines from source file and expected result from result file:

```
NODENAME NO_BUS_NAME$
    J1        79  U3      F1
```

should be converted into the line:

```
set_location_assignment PIN_F1 -to "NO_BUS_NAME"
```

```
NODENAME SINGLE_ENDED_BUS_21$
    J1        79  U3      AA3
```

should be converted into the line:

```
set_location_assignment PIN_AA3 -to "SINGLE_ENDED_BUS[21]"
```

```
NODENAME SINGLE_DIFF_P$
    J1        79  U3      B3
NODENAME SINGLE_DIFF_N$
    J1        79  U3      B4
```

should be converted into the line:

```
set_location_assignment PIN_B3 -to "SINGLE_DIFF"
set_location_assignment PIN_B4 -to "SINGLE_DIFF(n)"
```

If the `-o <output_file_name>` is not specyfied, the output file shoud take name after input file

## Netlist File:

The netlist file shoud be generated from Altium Designer using `File->Export->Netlist Schematic` and then selecting `Cadentix Netlist` as a netlist format. There are example [Netlist File](doc/input.net) for reference.

## Quartus File:

Quartus qsf file shoud be imported into project space without any changes. The pin assignments sqoud be visible in Pin Assignment View. There is example [Quartus File](doc/result.qsf) for reference.