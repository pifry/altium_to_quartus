Altium to Quartus netlist converter
===================================

The tool is made as an part of atomatic toolchain linking Altium Designer project to Quartus Prime project. The goal is to convert netlist names connected to FPGA in Altium Designer to Quartus Pin declaration in qsf file.

## Usage:

`altium_to_quartus -u U3 -o result.qsf input.net` 

This should generate new result.qsf from input.net file. Every line from input.net, that looks like this:

```
NODENAME LVDS_TOP_DATA.30_P$
    J1        79  U3      AH22
NODENAME LVDS_TOP_DATA.30_N$
    J1        79  U3      AH21
```

should be converted into the line:

```
set_location_assignment PIN_AH22 -to "LVDS_TOP_DATA[30]"
set_location_assignment PIN_AH21 -to "LVDS_TOP_DATA[30](n)"
```

in qsf file. Only lines with U3 should be considered. 

The program shoud check whether every line in source file that ends with _P have a line with the same name ending with _N. If not it shoud return non zero result, print missing nets and do not generate any output files.

The line:

```
NODENAME NO_BUS_NAME_N$
    J1        79  U3      F1
```

should be converted into the line:

```
set_location_assignment PIN_F1 -to "NO_BUS_NAME(n)"
```

## Netlist File:

The netlist file shoud be generated from Altium Designer using `File->Export->Netlist Schematic` and then selecting `Cadentix Netlist` as a netlist format. There are example [Netlist File](docs/input.net) and [Quartus File](docs/result.qsf) for reference.

## Quartus File:

Quartus qsf file shoud be imported into project space without any changes. The pin assignments sqoud be visible in Pin Assignment View.